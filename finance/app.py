import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio = []
    owned_stocks = db.execute(
        "SELECT stock, SUM (CASE WHEN transaction_type = 'Bought' THEN shares ELSE -shares END) as shares FROM purchases WHERE buyer_id = ? GROUP BY stock", session["user_id"])
    result = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    current_cash = round(float(result[0]["cash"]), 2)
    overall = 0
    for s in owned_stocks:
        stock_info = lookup(s["stock"])
        if stock_info:
            total_value = s["shares"] * stock_info["price"]
            if s["shares"] > 0:
                portfolio.append({
                    "Symbol": s["stock"],
                    "Shares": s["shares"],
                    "Value": stock_info["price"],
                    "Total": total_value,
                    "Cash": current_cash,
                })
            overall += total_value
    grand_total = overall + current_cash
    portfolio.append({
        "Overall": grand_total
    })
    cash = current_cash
    overall = grand_total
    portfolio.pop()
    return render_template("index.html", portfolio=portfolio, cash=cash, overall=overall)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    else:
        if not request.form.get("symbol") or not request.form.get("shares") or lookup(request.form.get("symbol")) == None or not request.form.get("shares").isdigit() or int(request.form.get("shares")) < 0:
            return apology("Please specify the number of shares, and a valid stock symbol", 400)
        else:
            logged_user = session["user_id"]
            stock_price = lookup(request.form.get("symbol"))["price"]
            current_cash = db.execute("SELECT cash FROM users WHERE id = ?",
                                      (logged_user,))[0]["cash"]
            no_stocks = int(request.form.get("shares"))
            cash_update = current_cash - (stock_price * no_stocks)
            if cash_update < 0:
                return apology("Insufficient funds", 400)
            else:
                # print(f"cash_update: {cash_update}, logged_user: {logged_user}")
                db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_update, logged_user)
                db.execute("INSERT INTO purchases (buyer_id, stock, stock_price, shares, transaction_type) VALUES (?, ?, ?, ?, 'Bought')",
                           logged_user, request.form.get("symbol").upper(), stock_price, no_stocks)

                return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        history = db.execute("SELECT * FROM purchases WHERE buyer_id = ?", session["user_id"])
        return render_template("history.html", history=history)

    else:
        # to create in history.html: loop through all the items in the list in Jinja, and create a <p> for every new item - showing: status,stock, price, shares, date
        # extra: use bootstrap to populate a table, when the rows are different coloured, altering, for better visibility
        return apology("Wrong request", 400)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")

    else:
        if not request.form.get("symbol"):
            return apology("Please enter a stock symbol", 400)
        else:
            symbol = request.form.get("symbol")
            stock = lookup(symbol)
        if stock:
            return render_template("quoted.html", stock=stock)
        else:
            return apology("Stock not found", 400)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Please provide a username to register", 400)
        elif len(db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))) != 0:
            return apology("Username already exists", 400)
        elif not request.form.get("password"):
            return apology("Please provide a password to register", 400)
        elif not request.form.get("confirmation"):
            return apology("Please confirm your password", 400)
        elif (request.form.get("password")) != (request.form.get("confirmation")):
            return apology("Password does not match", 400)

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?,?)", request.form.get(
                    "username"), generate_password_hash(request.form.get("password"))
            )
        except ValueError:
            return apology("Username already exists", 400)

        return redirect("/login")

    elif request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbol_dropdown = db.execute(
            "SELECT stock, SUM (CASE WHEN transaction_type = 'Bought' THEN shares ELSE -shares END) as sum_shares FROM purchases WHERE buyer_id = ? GROUP BY stock HAVING sum_shares > 0", session["user_id"])
        return render_template("sell.html", symbol_dropdown=symbol_dropdown)
    else:
        symbol_dropdown = db.execute(
            "SELECT stock, SUM (CASE WHEN transaction_type = 'Bought' THEN shares ELSE -shares END) as sum_shares FROM purchases WHERE buyer_id = ? GROUP BY stock HAVING sum_shares > 0", session["user_id"])
        stock_to_sell = request.form.get("symbol")
        no_stock_to_sell = int(request.form.get("shares"))

        result = db.execute(
            "SELECT SUM (CASE WHEN transaction_type = 'Bought' THEN shares ELSE -shares END) AS bought_shares FROM purchases WHERE buyer_id = ? AND stock = ?", session["user_id"], stock_to_sell)
        if result[0]["bought_shares"] == None:
            no_stock_bought = 0
        else:
            no_stock_bought = result[0]["bought_shares"]
        if no_stock_to_sell > no_stock_bought:
            print(no_stock_to_sell, no_stock_bought)
            return apology("You can only sell as many shares as you own", 400)
        else:
            stock_price = lookup(stock_to_sell)["price"]
            db.execute("INSERT INTO purchases (buyer_id, stock, stock_price, shares, transaction_type) VALUES (?, ?, ?, ?, 'Sold')",
                       session["user_id"], stock_to_sell, stock_price, no_stock_to_sell)
            current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            cash_update = stock_price * no_stock_to_sell + current_cash[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_update, session["user_id"])
            return redirect("/")


@app.route("/add_cash", methods=["POST"])
@login_required
def add_cash():
    cash_to_add = request.form.get("add_cash")
    try:
        result = int(cash_to_add)

    except ValueError:
        return apology("Error when adding cash", 400)

    if result < 0:
        return apology("You cannot add negative numbers to your cash", 400)

    db.execute("UPDATE users SET cash= cash+? WHERE id = ?", result, session["user_id"])
    return redirect("/")

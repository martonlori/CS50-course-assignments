from cs50 import get_float

while True:
    change = get_float("Change: ")
    if change >= 0:
        break

quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01
coins = 0

# remainder = remainder + (change % quarter)
# coins = coins + ((change - remainder) / quarter)

while change >= quarter:
    change -= quarter
    coins += 1
    change = round(change, 2)

while change >= dime:
    change -= dime
    coins += 1
    change = round(change, 2)

while change >= nickel:
    change -= nickel
    coins += 1
    change = round(change, 2)

while change >= penny:
    change -= penny
    coins += 1

print(coins)

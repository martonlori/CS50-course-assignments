import sys
import requests

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            n = float(sys.argv[1])
        except:
            sys.exit("No. of bitcoins should be a float value")

        else:
            try:
                r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
                bitcoin_price = r["bpi"]["USD"]["rate"].replace(",", "")

            except requests.RequestException:
                print("Error when querying the API")
                sys.exit("Error when querying the API")

            else:
                print(f"${(float(n) * float(bitcoin_price)):,.4f}")








main()

import sys
import requests





def bitcoin(a):
    try:
        b = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json") # get information of site
        c = b.json()
        oo = c["bpi"]["USD"]["rate_float"] # make price for that
        TT = a * oo
        return f"${TT:,.4f}"
    except requests.RequestException:
        return None






if len(sys.argv) == 2: # chack about argv with 2 len
    try:
        n = sys.argv[1]
        print(bitcoin(float(n))) # go to the bitcoin def
    except ValueError:
        sys.exit("Command-line argument is not a number")
else: # if arg is not 2 len (less or more)
    sys.exit("Missing command-line argument")

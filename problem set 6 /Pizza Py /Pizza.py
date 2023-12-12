import csv
import sys
from tabulate import tabulate





def table(n):
    try:
        with open(n) as f:
            a = csv.reader(f) # read information
            tab = tabulate(a, headers="firstrow", tablefmt="grid")
            return tab
    except FileNotFoundError:
        sys.exit("File does not exist")







if len(sys.argv) < 2: # check the inpute of user
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2: # check the inpute of user
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        print(table(sys.argv[1])) # make tble




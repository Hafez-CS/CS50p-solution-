import csv
import sys




def c(a, n):
    try:
        with open(a) as a:
            r = csv.DictReader(a) # read information of this inpute (file)
            with open(n, "w") as n: # we want to write to this file
                o = ["first", "last", "house"]
                u = csv.DictWriter(n, fieldnames = o) # read file with dictreader
                u.writeheader()
                for i in r:
                    x, y = i["name"].split(", ")
                    k = i["house"]
                    u.writerow({"first": y, "last": x, "house": k})
    except FileNotFoundError:
        sys.exit(f"Could not read {a}")






if len(sys.argv) < 3: # check the inpute user
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3: # check the inpute user
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        c(sys.argv[1], sys.argv[2])

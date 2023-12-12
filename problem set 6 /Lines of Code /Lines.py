import sys





def cl(n): # def for count lines
    try:
        a = 0
        with open(n, "r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""): # count it
                    a = a + 1
            return a
    except FileNotFoundError:
        sys.exit("File does not exist")







if len(sys.argv) < 2: #  check the inpute
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2: #  check the inpute
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")
    else:
        print(cl(sys.argv[1])) # count the lines (name)




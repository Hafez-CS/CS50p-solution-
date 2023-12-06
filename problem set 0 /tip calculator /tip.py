def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent / 100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    a = d.strip("$")  # drop the $
    d = float(a)  # make int
    return d


def percent_to_float(p):
    a = p.strip("%")  # drop %
    p = int(a)  # make int
    return p


main()

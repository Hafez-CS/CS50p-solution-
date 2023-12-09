ii = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]








while True:
    n = input("Date: ") # get input of user
    try:
        if "/" in n: # check about "/" (number of date)
            a, b, c = n.split("/")
        elif "," in n: # check abou ", " (word of date)
            d, c = n.split(", ")
            a, b = d.split(" ")
            a = (ii.index(a)) + 1
        if int(a) > 12 or int(b) > 31: # chack about days and months
            raise ValueError
    except(AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(c)}-{int(a):02}-{int(b):02}") # print it
        break

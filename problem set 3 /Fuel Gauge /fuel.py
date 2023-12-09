n = input("Fraction: ")  # get input of user


def yyy(n):
    while True:
        try:
            x, y = n.split("/") # convert it
            if 0 <= int(x)/int(y) <= 0.1: # chack about E
                 return("E")
            elif 0.9 <= int(x)/int(y) <= 1: # chack about F
                 return ("F")
            elif 0.1 < int(x)/int(y) < 0.9:
                 return (str(round(int(x)/int(y)*100)) + "%") # return the answer
        except (ValueError, ZeroDivisionError):
            n = input("Fraction: ") # again



n = yyy(n)


print(n)  # print it

def main():
    n = input("Fraction: ") # get inpute of user
    nn = convert(n) # convert it
    print(gauge(nn)) # print it






def convert(a):
    x, y = a.split("/") # splite with  "/"
    if int(x)/int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return int(int(x)/int(y) * 100)







def gauge(a):
    try: # check about error
        if 0 <= a <= 1:
            return "E"
        elif 99 <= a <= 100:
            return "F"
        elif 1 < a < 99:
            return f"{int(a)}%"
        else:
            raise TypeError
    except TypeError:
        pass






if __name__ == "__main__":
    main()
def main():
    time = input("What time is it? ") # get the time of user
    if 7.0 <= convert(time) <= 8.0: # check with breakfast time
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0: # check with lunch time
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0: # check with dinner time
        print("dinner time")
    else:
        return


def convert(time):
    a, b = time.split(":") #convert to the real time
    h = float(a)
    m = float(b) * 1 / 60
    return float(h+m)


if __name__ == "__main__":
    main()

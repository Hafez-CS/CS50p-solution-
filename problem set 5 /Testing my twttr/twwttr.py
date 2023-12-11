def main():
    n = input("Input: ") # get inpute of user
    nn = shorten(n) # go to this def
    print(f"Output: {nn}") # print it









def shorten(a):
    sound = ["o", "a", "e", "i", "u"] # we need these sounds
    list = [] # a empty list
    for q in a:
        if q.casefold() not in sound: # find sounds
            list.append(q) # add to the list
    output = str("".join(list)) # outpute for print it
    return output











if __name__ == "__main__":
    main()
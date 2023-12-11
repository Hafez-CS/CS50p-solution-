def main():
    n = input("Plate: ") # get inpute of user
    if is_valid(n): # go to the def
        print("Valid")
    else:
        print("Invalid")




def is_valid(a):
    if 2 <= len(a) <= 6 and a.isalnum(): # check about len
        if a.isalpha():
            return True
        else:
            if a[:2].isalpha() and a[-2:].isdigit():
                for u in range(len(a)):
                    if a[u].isdigit():
                        if a[u].startswith("0") or a[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False






if __name__ == "__main__":
    main()
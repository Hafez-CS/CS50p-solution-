import re
import sys




def main():
    print(validate(input("IPv4 Address: "))) # get inpute of user




def validate(ip):
    n = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    a = re.search(r"^" + n + "\." + n + "\." + n + "\." + n + "$", ip) # check with searching
    if a:
        return True
    else:
        return False





if __name__ == "__main__":
    main()
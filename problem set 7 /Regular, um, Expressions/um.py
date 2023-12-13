import re
import sys



def main():
    print(count(input("Text: "))) # get inpute of user





def count(s):
    n = "(^|\W)um($|\W)"
    a = re.findall(n, s, re.IGNORECASE) # check for test
    if a:
        return(len(a))




if __name__ == "__main__":
    main()
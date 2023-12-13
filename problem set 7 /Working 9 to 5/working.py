import re
import sys



def main():
    print(convert(input("Hours: "))) # get inpute of user





def convert(s):
    n = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    a = re.search(r"^" + n + " to " + n + "$", s) # ceck with search option
    if a:
        b = jj(a.group(1), a.group(2), a.group(3))
        pt = jj(a.group(4), a.group(5), a.group(6))
        return f"{b} to {pt}"
    else:
        raise ValueError








def jj(h, m, s): # check for outpute
    if h == "12":
        if s == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if s == "AM":
            hour = f"{int(h):02}"
        else:
            hour = f"{int(h)+12}"
    if m == None:
        i = "00"
    else:
        i = f"{int(m):02}"
    return f"{hour}:{i}"







if __name__ == "__main__":
    main()
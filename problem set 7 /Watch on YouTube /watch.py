import re
import sys




def main():
    print(parse(input("HTML: "))) # get inpute of user




def parse(s):
    if link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s): # check with search
        return f"https://youtu.be/{link.group(2)}"
    else:
        return None




if __name__ == "__main__":
    main()

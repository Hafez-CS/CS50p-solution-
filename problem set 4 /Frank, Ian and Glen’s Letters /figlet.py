import sys
import random
from pyfiglet import Figlet



fi = Figlet()
c = ["-f", "--font"] # can choice the fonts



def mama():
    if len(sys.argv) < 2: # without new font
        a = random.choice(fi.getFonts())
        ii(a)
    elif len(sys.argv) > 2 and sys.argv[1] in c and sys.argv[2] in fi.getFonts(): # with new font , user change it
        a = sys.argv[2]
        ii(a)
    else:
        sys.exit("Invalid usage")



def ii(fo): # print it with new font or random font
    r = input("Input: ")
    fi.setFont(font=fo)
    print("Output:")
    print(fi.renderText(r))


mama()

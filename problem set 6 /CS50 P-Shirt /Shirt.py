from PIL import Image, ImageOps
import sys
import os





def change_photo(a, b):
    try:
        n = Image.open("shirt.png") # do to the this value
        with Image.open(a) as a: # open the photo
            ic = ImageOps.fit(a, n.size)
            ic.paste(n, mask = n) # user import
            ic.save(b)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")






if len(sys.argv) < 3: # check the inpute of user
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3: # check the inpute of user
    sys.exit("Too many command-line arguments")
else:
    ii = [".jpg", ".jpeg", ".png"] # for check whats we have.
    kk = os.path.splitext(sys.argv[1])
    oo = os.path.splitext(sys.argv[2])
    if oo[1].lower() not in ii:
        sys.exit("Invalid output")
    elif kk[1].lower() != oo[1].lower():
        sys.exit("Input and output have different extensions")
    else:
        change_photo(sys.argv[1], sys.argv[2]) # go to the function

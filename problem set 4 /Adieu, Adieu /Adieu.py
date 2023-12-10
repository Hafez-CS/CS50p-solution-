import inflect



a = inflect.engine()
b = []




while True:
    try:
        c = input("Name: ") # get inpute of user
        b.append(c) # add to the b list
    except EOFError:
        print("Adieu, adieu, to", a.join(b)) # print all of them
        break

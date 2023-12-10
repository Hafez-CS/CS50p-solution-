import random





def main():
    a = 10
    b = 0
    c = 3
    l = get_level()
    while a != 0:
        if c == 3:
            x, y = generate_integer(l) # random number for test
        try:
            ag = int(input(f"{x} + {y} = ")) # get input of user
            rr = x + y
            if ag == rr: # check the user answer
                a = a - 1
                b = b + 1
                c = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            c = c - 1
            pass
        if c == 0:
            print((f"{x} + {y} = {rr}")) # print the right answer
            c = 3
            a = a - 1
            continue
    print("b:" , str(b))






def get_level(): # get level of user fo start game
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass






def generate_integer(uu): # make random number for testing
    if uu == 1: # for level 1
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    if uu == 2: # for level 2
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    if uu == 3: # for level 3
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y





if __name__ == "__main__":
    main()

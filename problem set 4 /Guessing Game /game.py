import random




while True:
    try:
        a = int(input("Level: "))
        b = random.randint(0, a) # random number
        while True:
            c = int(input("Guess: "))
            if c > b: # check about "tool large"
                print("Too large!")
            elif c < b: # chack about "too small"
                print("Too small!")
            elif c == b: # check about "just right"
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break

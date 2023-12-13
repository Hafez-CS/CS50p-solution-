import validators
import sys



def main():
    print(validate(input("What's your email address? "))) # get inpute of user




def validate(s):
    if validators.email(s) == True: # check fot testing
        return f"Valid"
    else:
        return f"Invalid"




if __name__ == "__main__":
    main()

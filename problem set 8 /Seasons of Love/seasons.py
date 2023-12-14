from datetime import date
import inflect
import sys
import operator



n = inflect.engine()
def main():
    try:
        o = input("Date of Birth: ") # et inpute about dae of Birthday
        i = operator.sub(date.today(), date.fromisoformat(o))
        print(cv(i.days))
    except ValueError:
        sys.exit("Invalid date")




def cv(time):
    a = time * 24 * 60 #convert it
    return f"{(n.number_to_words(a, andword='')).capitalize()} minutes"





if __name__ == "__main__":
    main()
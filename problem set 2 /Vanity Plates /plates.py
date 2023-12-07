def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")






def is_valid(s):

    if 2 <= len(s) <= 6 and s.isalnum(): # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

        if s.isalpha():
            return True
        else:

            if s[:2].isalpha() and s[-2:].isdigit(): # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
                for i in range(len(s)):

                    if s[i].isdigit():

                        if s[i].startswith("0") or s[i:].isalpha(): # The first number used cannot be a ‘0’.”
                            return False
                        else:
                            return True

            else:
                return False

    else:
        return False


main()

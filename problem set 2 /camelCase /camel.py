n = input("camelCase: ") # get name of user

n = "".join(["_" + a.lower() if a.isupper() else a for a in n]).strip("_") # convert name to this (namefirst == name_first)

print("snake_case: ",n) # print it

n = input("Greeting: ")

a = n.find("Hello")
b = n.find("hello")
c = n.startswith("h")
d = n.startswith("H")

if a != -1 or b != -1:
    print("$0")
elif c == True or d == True:
    print("$20")
else:
    print("$100")

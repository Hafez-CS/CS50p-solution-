n = input("Expression: ")

a = n.find("+")
b = n.find("-")
c = n.find("*")
d = n.find("/")


if a != -1:
    q = n.split()
    w = float(q[0])
    e = float(q[2])
    print(w + e)

elif b != -1:
    q = n.split()
    w = float(q[0])
    e = float(q[2])
    print(w - e)

elif c != -1:
    q = n.split()
    w = float(q[0])
    e = float(q[2])
    print(w * e)


elif d != -1:
    q = n.split()
    w = float(q[0])
    e = float(q[2])
    print(w / e)

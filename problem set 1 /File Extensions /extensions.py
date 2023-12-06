n = input("file name: ")

a = n.find(".gif")
b = n.find(".jpg")
c = n.find(".jpeg")
d = n.find(".png")
f = n.find(".pdf")
ff = n.find(".PDF")
g = n.find(".txt")
h = n.find(".zip")



if a != -1:
    print("image/gif")
elif b != -1:
    print("image/jpeg")
elif c != -1:
    print("image/jpeg")
elif d != -1:
    print("image/png")
elif f != -1 or ff != -1:
    print("application/pdf")
elif g != -1:
    i = n.strip('.txt')
    print("text/"+i)
elif h != -1:
    print("application/zip")
else:
    print("application/octet-stream")

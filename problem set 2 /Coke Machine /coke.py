c = [25, 10, 5]
a = 50
b = 0
while a > 0:
    print("Amount Due:" , a) # show the price of coke
    d = int(input("Insert Coin: ")) # inter the dollars of the price
    if d in c: # convert it
        a = a - d
        b = b + d
if b >= a:
    print(f"Change Owed: {b - 50}")

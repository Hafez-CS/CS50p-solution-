a = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

s = 0

while True:
    try:
        n = input("Item: ").title()
        s = s + a[n]
        print(f"Total: ${s:.2f}")
    except EOFError:
        print()
        break
    except KeyError:
        pass

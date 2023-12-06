n = input("what is the answer to the great question of life, the universe, and everything? ")


a = n.find("42")

if a != -1:
    n = '42'


if n == '42':
    print("Yes")
elif n == 'Forty Two':
    print("Yes")
elif n == 'forty-two' :
    print("Yes")
elif n == 'forty two':
    print("Yes")
elif n == 'FoRty TwO':
    print("Yes")
elif n == '50':
    print("No")
elif n == 'fifty':
    print('NO')

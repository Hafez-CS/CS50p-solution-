n = input("Input: ")


n = n.translate({ord('o'): None})
n = n.translate({ord('O'): None})
n = n.translate({ord('a'): None})
n = n.translate({ord('e'): None})
n = n.translate({ord('i'): None})
n = n.translate({ord('u'): None})

print(n)

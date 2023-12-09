a = {}






while True:
    try:
        item = input().upper()
        if item not in a:  # if this item is not exist
            a[item] = 1
        else:  # if its exist
            a[item] = a[item] + 1
    except EOFError: # if user click control+d
        f = dict(sorted(list(a.items()))) # sorted of list
        for s in f:
            print(f[s], s, sep=" ") # print it
        break
    except KeyError:
        pass

def sum_list(a):
    total = 0
    for i in a:
        if i.isnumeric():
            total = total + i
        else:
            pass
    return total

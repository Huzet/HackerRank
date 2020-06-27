def myround(x, base=5):
    return base * round(x/base)

def newround(x, base=5):
    while x % 5 != 0:
        x = x + 1
    return x

# 67 73
# 2 * 3 = 6 multiply
# 6 / 3 = 2 devide
# 12 % 7 = 5 Modulous


test = map(newround, (73, 67, 38, 33))
print(list(test))
# print(round(7))
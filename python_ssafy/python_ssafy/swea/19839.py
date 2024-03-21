n = int(input())
def co(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return co(x/2) + 1
    return co(3*x + 1) + 1
print(co(n))
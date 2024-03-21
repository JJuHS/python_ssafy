n = int(input())

def a(x):
    if x < 10:
        return x
    return x % 10 + a(x // 10)

print(a(n))
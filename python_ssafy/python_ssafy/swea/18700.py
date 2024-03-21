n, m = map(int, input().split())
vodca = [list(map(int, input().split())) for _ in range(m)]

six = 1000
one = 1000
for price in vodca:
    one = min(one, price[1])
    six = min(six, price[0])
if six < 6 * one:
    print(min((six*(n//6) + one*(n%6)), six*((n//6)+1)))
else:
    print(n)


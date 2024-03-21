import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
s = [sys.stdin.readline().strip() for _ in range(36)]


ans = 'Valid'
while True:
    if len(set(s)) != 36:
        ans = 'invalid'
        break

    for i in range(36):
        f = s[i]
        if i == 35:
            i = -1
        e = s[i+1]

        if not (1 <= abs(int(f[1])-int(e[1])) <= 2):
            ans = 'invalid'
            break

        if abs(int(f[1]) - int(e[1])) + abs(alphabet.index(f[0]) - alphabet.index(e[0])) != 3:
            ans = 'invalid'
            break

    break

print(ans)

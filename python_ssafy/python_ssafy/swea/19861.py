N = int(input())
X = list(map(int, input().split()))


def find101(n, x, ans = '', idx = 0, res = 0, pr = 0):
    if idx == 0:
        ans = str(x[0])
        res = x[0]
        pr = x[0]
        find101(n, x, ans, idx+1, res, pr)

    if idx == n:
        if res % 101 == 0 and res != 0:
            print(ans)
        return

    find101(n, x, ans + '*' + str(x[idx]), idx + 1, res * x[idx], pr * x[idx])
    find101(n, x, ans + '+' + str(x[idx]), idx + 1, res + x[idx], x[idx])
    find101(n, x, ans + '-' + str(x[idx]), idx + 1, res - x[idx], x[idx])

find101(N, X)
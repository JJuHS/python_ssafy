def inorder(x, i = 1):
    global inord
    if i <= x:
        inorder(x, i * 2)
        inord.append(i)
        inorder(x, i * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(range(1, n + 1))
    inord = []
    inorder(n)

    ans1 = arr[inord.index(1)]
    ans2 = arr[inord.index(n//2)]
    print(f'#{tc} {ans1} {ans2}')
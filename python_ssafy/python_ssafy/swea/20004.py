N, M = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
numbers.sort(key = lambda x:abs(x), reverse = True)
res = 10 ** 6, []
visited = [False] * N

def min_is(arr, m, ans = 1, ans_tmp = []):
    global res
    if m == 0:
        if res[0] > ans:
            res = ans, ans_tmp[:]
            return
        return
    ans_tmp = ans_tmp[:]

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            s = arr.pop(i)
            ans_tmp.append(s)
            ans *= s
            min_is(arr, m - 1, ans, ans_tmp)
            visited[i] = False
            arr.insert(i, s)
            ans //= s
            ans_tmp.pop()

min_is(numbers, M)
arr = res[1]
arr.sort()
print(*arr)

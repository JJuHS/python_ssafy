n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

cnt = 0
start = arr[0]-1

for i in arr:
    if i > start:
        cnt += 1
        start = i + l - 1

print(cnt)
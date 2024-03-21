n, k = map(int, input().split())

divide_list = [int(input()) for _ in range(n)]
start = 1
end = max(divide_list)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt += divide_list[i] // mid
    if cnt >= k:
        start = mid + 1
    else:
        end = mid - 1
print(end)
n = int(input())
n_list = list(map(int, input().split()))
k = int(input())
k_list = list(map(int, input().split()))
ans = ''
for num in k_list:
    if num in n_list:
        ans += 'O'
    else:
        ans += 'X'
print(ans)
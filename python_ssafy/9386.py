T = int(input())
for tc in range(1,T+1):
    n = int(input())
    numbers = input()
    ans = 0
    ans_tmp = 0
    for i in range(n):
        if numbers[i] == '0':
            ans = max(ans, ans_tmp)
            ans_tmp = 0
        else:
            ans_tmp += 1
        ans = max(ans, ans_tmp)
    print(f'#{tc}',ans)

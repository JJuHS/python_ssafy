T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    str_list = [list(input()) for _ in range(n)]
    ans = ''

    for str_ in str_list:
        for i in range(0,n-m+1):
            str_tmp = str_[i:i+m]
            if str_tmp == str_tmp[::-1]:
                ans = str_tmp

    if ans == '':
        str_list2 = [[''] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                str_list2[j][i] = str_list[i][j]
        for str_ in str_list2:
            for i in range(0, n - m + 1):
                str_tmp = str_[i:i + m]
                if str_tmp == str_tmp[::-1]:
                    ans = str_tmp
    print(f'#{tc}', ''.join(ans))
s = list(input())
ans = 0

while (len(s) - 1) // 2:
    for i in range(len(s)):
        if s[i] == '+':
            ans = int(s[i - 2]) + int(s[i - 1])
            s.pop(i)
            s.pop(i-2)
            s[i-2] = ans
            break

        if s[i] == '-':
            ans = int(s[i - 2]) - int(s[i - 1])
            s.pop(i)
            s.pop(i-2)
            s[i-2] = ans
            break

print(ans)
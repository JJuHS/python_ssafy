T = int(input())

def forth(x):
    stack = []
    for i in x:
        if i == '.':
            break
        if i.isdigit():
            stack.append(int(i))
        else:
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            if i == '-':
                stack.append(a - b)
            if i == '*':
                stack.append(a * b)
            if i == '/':
                if b == 0:
                    return 'error'
                stack.append(a / b)
    if len(stack) != 1:
        return 'error'
    return stack.pop()

for tc in range(1, T + 1):
    arr = list(map(str, input().split()))
    ans = forth(arr)
    print(f'#{tc} {ans}')
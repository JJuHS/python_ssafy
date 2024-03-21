T = int(input())
for tc in range(1, T+1):
    x = input()
    stack = []
    for i in x:
        if i == '(' or i == '{':
            stack.append(i)

        if i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        if i == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
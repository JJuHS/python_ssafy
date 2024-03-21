str_list = input()
ans = 0
str_list = str_list.replace('}','{')
str_list = str_list.replace(']','[')
ans_list = []
for str_ in str_list:
    ans_list.append(str_)

    if ans_list.count('[') == 0:
        ans_list.pop()
    if ans_list.count('[') == 2:
        ans += int(''.join(ans_list[1:-1]))
        ans_list.clear()

    ans_list.append(str_)
    if ans_list.count('{') == 0:
        ans_list.pop()
    if ans_list.count('{') == 2:
        ans *= int(''.join(ans_list[1:-1]))
        ans_list.clear()

print(ans)
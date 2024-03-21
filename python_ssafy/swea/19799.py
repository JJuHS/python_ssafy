year, month, day = map(str, input().split('.'))
ans_1 = 0
ans_2 = 0
if len(month) == 1:
    if month == 'X':
        ans_1 = 9
if len(month) == 2:
    if month[1] == 'X':
        ans_1 = 3

if len(day) == 1:
    if day == 'X':
        ans_2 = 9
if len(day) == 2:
    if day[1] == 'X' and day[0] == 'X':
        ans_2 = 22
    else:
        if day[1] == 'X':
            ans_2 = 10
        if day[0] == 'X':
            if day[1] == '0' or day[1] == '1':
                ans_2 = 3
            else:
                ans_2 = 2

if 0 in [ans_2, ans_1]:
    print(max(ans_1, ans_2))
else:
    print(ans_1*ans_2)




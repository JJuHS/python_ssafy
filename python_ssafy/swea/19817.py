str_ = input()

idx = min(str_.index('-'), str_.index('+'))
if idx == 0:
    idx = min(str_[1:].index('-'), str_.index('+'))

ans = int(str_[:idx])

for i in range(idx + 1,len(str_)):
    if str_[i] == '-' or str_[i] == '+':
        if str_[idx] == '+':
            ans += int(str_[idx+1:i])
        if str_[idx] == '-':
            ans -= int(str_[idx+1:i])
        idx = i
    if i == len(str_)-1:
        if str_[idx] == '+':
            ans += int(str_[idx+1:i+1])
        if str_[idx] == '-':
            ans -= int(str_[idx+1:i+1])
print(ans)
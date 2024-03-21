T = int(input())

def del_word(word_):
    if len(word_) == 0:
        return 0
    if len(word_) == 1:
        return 1

    for i in range(len(word_) - 1):
        if word_[i] == word_[i + 1]:
            word_.pop(i)
            word_.pop(i)
            del_word(word_)
            break

    return len(word_)

for tc in range(1, T + 1):
    word = list(input())
    ans = del_word(word)
    print(f'#{tc} {ans}')

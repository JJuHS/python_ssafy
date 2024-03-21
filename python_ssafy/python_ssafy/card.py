T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    card = input()
    card_list = sorted([int(char) for char in card])
    card_num_list = [0]*10

    for i in card_list:
        card_num_list[i] += 1
    max_num = max(card_num_list)
    card_is = 0
    for i in range(9, 1, -1):
        if card_num_list[i] == max_num:
            card_is = i
            break


    print(f'#{tc} {card_is} {max_num}')


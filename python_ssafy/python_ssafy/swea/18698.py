money = int(input())
coin_list = [500, 100, 50, 10]
return_list = []
for coin in coin_list:
    while True:
        if money >= coin:
            money -= coin
            return_list.append(coin)
        else:
            break
print(len(return_list))
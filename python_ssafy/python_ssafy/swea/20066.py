def game(x, y):
    if x[1] == y[1] and x[0] < y[0]:
        return x
    if (x[1], y[1]) in [(1, 3), (2, 1), (3, 2)]:
        return x
    return y

def game_group(Arr):
    if len(Arr) == 1:
        return Arr
    if len(Arr) == 2:
        return [game(Arr[0], Arr[1])]
    p = (1 + len(Arr))//2
    return game_group(game_group(Arr[p:]) + game_group(Arr[:p]))

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [(i + 1, j) for i, j in enumerate(list(map(int, input().split())))]
    print(f'#{tc} {game_group(arr)[0][0]}')
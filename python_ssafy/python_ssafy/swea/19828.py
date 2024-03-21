T = int(input())

def paper(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    return 2 * paper(x-2) + paper(x-1)


for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc} {paper(n/10)}')
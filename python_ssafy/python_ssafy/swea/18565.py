def score(n, arr, visited, score_tmp):
    global max_score

    if all(visited):
        max_score = max(score_tmp, max_score)

    for i in range(n):
        if not visited[i]:
            left = i - 1
            right = i + 1
            current = 1
            while left >= 0:
                if not visited[left]:
                    current = arr[left]
                    break
                left -= 1
            while right < n:
                if not visited[right]:
                    current *= arr[right]
                    break
                right += 1

            if left < 0 and right > n-1:
                current = arr[i]
            visited[i] = True
            score(n, arr, visited, current + score_tmp)
            visited[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    balloon_list = list(map(int, input().split()))
    max_score = 0
    visited = [False] * N
    score(N, balloon_list, visited, 0)
    print(f'#{tc} {max_score}')

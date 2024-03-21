T = int(input())

def BackTracking(cnt = 0, tmp = 0):
    global res
    if cnt == n: # 모든 가로줄을 탐색한 경우 종료
        res = max(tmp, res) # 최댓값 갱신
        return

    for i in range(n):  # 세로 cnt 가로 i 로 설정
        if not visited[i]:  # 가본 적 없는 세로줄
            if arr[cnt][i] >= 0:
                visited[i] = 1
                BackTracking(cnt + 1, tmp + arr[cnt][i])    # 새로운 가로줄에서 다시 탐색
                visited[i] = 0  # 이번 가로줄에서 새로운 선택을 위해 다시 '미방문' 으로 처리

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = -10 ** 6     # 최댓값 초기화
    visited = [0] * n
    BackTracking()

    print(f'#{tc} {res}')

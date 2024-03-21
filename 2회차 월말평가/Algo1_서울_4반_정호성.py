T = int(input())

def work(s):
    i, j, w = s[0] - 1, s[1], s[2] # [i, j, w] = [위치, 돌 개수, 작업번호]
    if w == 1:  # 작업번호 1 : i부터 j개를 모두 뒤집기
        for k in range(i, i + j):
            if k >= n:
                return
            arr[k] = 1 - arr[k]
        return

    elif w == 2:     # 작업번호 2 : i부터 j개를 i번 상태랑 같게 만들기
        criteria = arr[i]
        for k in range(i, i + j):
            if k >= n:
                return
            arr[k] = criteria
        return

    else:    # 작업번호 3: i번 부터 1 ~ j 만큼의 거리의 두 돌을 비교하여 같으면 둘다 뒤집음
        for k in range(1, j + 1):
            left = i - k
            right = i + k
            if 0 <= left < n and 0 <= right < n:
                if arr[left] == arr[right]:
                    arr[left], arr[right] = 1 - arr[left], 1 - arr[right]
                continue
            return
        return

for tc in range(1, T + 1):
    n, m = map(int, input().split())    # 돌 개수, 작업 개수
    arr = list(map(int, input().split()))   # 돌의 현재상태

    for _ in range(m):      # 모든 작업에 대해 함수 실행
        wo = list(map(int, input().split())) # [i, j, w] = [위치, 돌 개수, 작업번호]
        work(wo)

    print(f'#{tc}', *arr)

T = int(input())
direction = [(1, 0), (0, 1), (1, 1)]

def find_max(s = (0, 0)):   # m X m 배열에서 최대값 찾기
    ans = arr[s[0]][s[1]]   # 최댓값 초기화
    idx_tmp = s # 최댓값의 조표 초기화
    for i in range(s[0], s[0] + m): # x 범위
        for j in range(s[1], s[1] + m): # y 범위
            if 0 <= i < n and 0 <= j < n:   # n X n 행렬 내부인지 확인
                if ans < arr[i][j]: # 최댓값인 경우 갱신
                    ans = arr[i][j]
                    idx_tmp = (i, j)
    return idx_tmp, ans # 최댓값의 좌표와 최댓값 반환


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = (0, 0)    # 시작지점
    max_num = arr[0][0]
    total_sum = 0   # 누적 합
    cnt = 0 # 누적된 합의 개수

    while True:
        res_tmp, max_num = find_max(res)    # 매번 새로운 시작점에 대해 반복
        if res_tmp == res:  # 시작값의 값이 최대인 경우 종료
            break
        cnt += 1
        total_sum += max_num    # 새로운 최댓값을 누적합에 합산
        res = res_tmp   # 새로운 시작 좌표 지정

    if cnt == 0:    # 최댓값이 원점으로 끝나는 경우
        total_sum = max_num

    print(f'#{tc} {total_sum}')

def score(ans, pro):
    score = 0
    current = 1
    for i in range(len(pro)):
        if ans[i] == pro[i]:
            score += current
            current += 1
        else:
            current = 1
    return score

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    ans = list(map(int, input().split()))
    student_ans = [list(map(int, input().split())) for _ in range(n)]
    result_max = 0
    result_min = 999
    for submit in student_ans:
        result_max = max(result_max, score(ans, submit))
        result_min = min(result_min, score(ans, submit))
        result = result_max - result_min
    print(f'#{tc} {result}')


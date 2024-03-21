import sys
n = int(input())
student_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
meet_list = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        for k in range(5):
            if student_list[i][k] == student_list[j][k]:
                meet_list[i][j] = 1
                meet_list[j][i] = 1

ans_list = []

for i in range(n):
    ans_list.append(sum(meet_list[i]))

print(ans_list.index(max(ans_list)) + 1)

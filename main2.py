import sys
from collections import deque as dq
input = sys.stdin.readline
n, m = map(int, input().split())
ladder = []
snake = []
for _ in range(n):
    ladder.append(list(map(int, input().split())))
for _ in range(m):
    snake.append(list(map(int, input().split())))

q = dq()
q.append(1)
arr = [0] * 101
visited = [0] * 101


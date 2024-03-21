import sys
from collections import deque

n, m = map(int, input().split())
pop_list = map(int, sys.stdin.readline().split())
my_que = deque([i for i in range(1, n+1)])
cnt = 0

for num in pop_list:
    while True:
        if my_que[0] == num:
            my_que.popleft()
            break
        else:
            if my_que.index(num) < len(my_que)/2:
                while my_que[0] != num:
                    my_que.append(my_que.popleft())
                    cnt += 1
            else:
                while my_que[0] != num:
                    my_que.appendleft(my_que.pop())
                    cnt += 1
print(cnt)

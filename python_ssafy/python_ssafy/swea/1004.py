import sys
from math import dist
# def distance(x,y):
#     res = ((x[0]-x[1])**2+(y[0]-y[1])**2)**0.5
#     return res


T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    astro = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = 0
    st2 = [x1, y1]
    st3 = [x2, y2]
    for i in astro:
        st1 = [i[0], i[1]]
        dist1 = dist(st1, st2) - i[2]
        dist2 = dist(st1, st3) - i[2]
        if dist1*dist2 < 0:
            ans += 1
    print(ans)
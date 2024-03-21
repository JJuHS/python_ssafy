import sys
for i in sys.stdin.readlines():
    print("NY"[int(i) % 6 == 0])

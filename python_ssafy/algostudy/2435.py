import sys
n, k = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

sum_temperature = [sum(temperature[i:i+k]) for i in range(n-k+1)]
print(max(sum_temperature))

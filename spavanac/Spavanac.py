import sys
h,m = map(int, sys.stdin.readline().split())

newm = m - 45

if newm < 0:
    h-=1

print(h%24, newm%60)

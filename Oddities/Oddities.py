import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    print(f"{x} is " + ("even" if x%2 == 0 else "odd"))
    
    
    #first iteration
    #if x % 2 == 0:
     #   print(f"{x} is even")
   # if x % 2 != 0:
    #    print(f"{x} is odd")

import sys

N = int(input())
if N < 0 or N >100: 
    sys.exit()

for i in range(1,N+1,1): 
    for j in range(N-i,0,-1):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print("")
for i in range(N-1,0,-1): 
    for j in range(0,N-i,1):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print("")
import sys
count = int(input())
for c in range(1,count+1):
    list_str = sys.stdin.readline().rstrip().split()
    list_int = list(map(int,list_str))
    print(f"Case #{c}: {sum(list_int)}")
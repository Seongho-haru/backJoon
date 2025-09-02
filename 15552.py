import sys
count = int(input())
for c in range(count):
    list_str = sys.stdin.readline().rstrip().split()
    num_list = list(map(int,list_str))
    print(sum(num_list))
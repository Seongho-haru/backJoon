import sys
list_strs =[ line.rstrip() for line in sys.stdin.readlines()]
for line in list_strs:
    list_int = list(map(int, line.split()))
    print(sum(list_int))
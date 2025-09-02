from typing import List
num_list: List[int] = list(map(int,input().split()))
num_set = set(num_list)

if len(num_set) == 3:
    num_list.sort()
    print(num_list.pop()*100)
elif len(num_set) == 2:
    same_num = sum(num_list) - sum(num_set)
    print(same_num*100 + 1000)
elif len(num_set) ==1:
    print(num_set.pop()*1000 + 10000)
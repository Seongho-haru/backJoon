year = int(input())

def is_leap(year: int) -> int: 
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    return 0

print(is_leap(year))
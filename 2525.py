from datetime import datetime,timedelta

h , m = map(int, input().split())
add_min = int(input())

def isValidHour(hour: int)-> int:
    if hour >= 0 and hour <=23:
        return hour
    raise ValueError("시간은 0과 23사이에 있어야합니다.")

def isValidMinute(minute: int)-> int:
    if minute >=0 and minute <= 59:
        return minute
    raise ValueError("분은 0과 59분사이에 있어야합니다.")

def isValidAddMinute(minute: int)-> int:
    if minute >=0 and minute <= 1000:
        return minute
    raise ValueError("추가시간은 0과 100분사이에 있어야합니다.")

time = datetime(
    year=200,
    month=1,
    day=1,
    hour= isValidHour(hour=h),
    minute= isValidMinute(minute=m)
    )

time_edit = time + timedelta(minutes=isValidAddMinute(add_min))
print(f"{time_edit.hour} {time_edit.minute}")
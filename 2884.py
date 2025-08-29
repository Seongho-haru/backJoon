from datetime import datetime ,timedelta

def sub_time_45m(h: int , m: int):
    edit_time = datetime(year=2000,month=1,day=1,hour=h,minute=m)
    edit_time -= timedelta(minutes=45)
    return f"{edit_time.hour} {edit_time.minute}" 


if __name__ == "__main__":
    h , m = map(int,input().split())
    print(sub_time_45m(h,m))
    
    
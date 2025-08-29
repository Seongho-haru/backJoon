a = int(input())
b = int(input())

def gcd (a: int , b:int )-> int:
    if a > 0 and b > 0:
        return 1
    elif a < 0 and b > 0:
        return 2
    elif a < 0 and b < 0:
        return 3
    elif a > 0 and b < 0:
        return 4
    
print(gcd(a,b))
        
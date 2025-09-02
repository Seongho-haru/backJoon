#첫째 줄에는 영수증 적힌 총 금액 X

#두번째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N

#이후 N개의 줄에는 각물건의 가격 A와 개수b가 공백을 사이에 두고 주어진다.

total_price = int(input())
count = int(input())

sum_price = 0
for c in range(count):
    price , count = map(int,input().split())
    sum_price += (price*count)

if total_price == sum_price:
    print("Yes")
else:
    print("No")
#백준 2588
A= int(input())
B = int(input())
#B숫자를 자리별로 리스트로 만듬
B_list = list(str(B))

#B리스트를 역순으로 n변수에 넣어서 계산
for n in B_list[::-1]:
    print(A*int(n))
print(A*B)
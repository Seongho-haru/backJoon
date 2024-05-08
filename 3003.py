#백준 3003
correctAnswer = [1,1,2,2,2,8]

answer = input().split()

result = ""
for an , an_c in zip(answer,correctAnswer):
    result+=str(int(an_c)-int(an))
    result +=" "
print(result)
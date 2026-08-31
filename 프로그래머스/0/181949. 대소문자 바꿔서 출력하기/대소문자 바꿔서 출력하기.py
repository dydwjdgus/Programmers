i = []
str = input()
#1.문자를 받는다.
#2.리스트로 나누기
#3.리스트 원소를 하나씩 k에 넣기
#4.k가 대문자인지 판별하기
#5.대문자라면 lower()로 반환하기

i = list(str)


for k in i:
    if k.isupper():
        print(k.lower(),end='')
    else:
        print(k.upper(),end='')
#정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
a = int(input())
while True:
    if a == 0:
        break
    a -= 1
    print(a)


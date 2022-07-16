
#입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
#단, 3항 연산을 사용한다.

a, b, c = map(int, input().split())

if a > b > c:
    print(c)
elif a > c > b:
    print(b)
elif b > c > a:
    print(a)
elif b > a > c:
    print(c)
elif c > a > b:
    print(b)
elif c > b > a:
    print(a)
elif a  == b > c:
    print(c)
elif b == c > a:
    print(a)
elif c == a > b:
    print(b)
else:
    print(a)

#정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.

a, b = map(int, input().split())
c = (2 ** b)
d = a * c
print(d)


a, b = map(int, input().split())
print(a << b)
# << = 2의 b 거듭제곱
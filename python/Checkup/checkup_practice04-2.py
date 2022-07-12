#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오
a = int(input())
n = 0
result = 1
while n < a:
    n += 1
    result *= n
print(result)


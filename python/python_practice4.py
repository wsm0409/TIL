#1부터 사용자가 입력한 양의 정수까지 총합을 구하는 코드를 작성하시오.

a = 0
result = 0
user_input = int(input())

while a < user_input:
    a += 1
    result += a
print(result)



#주어진 숫자의 평균을 구하는 코드를 작성하시오.

#input numbers = [3, 10, 20]
#output = 11

numbers = [3, 10, 20]
result = 0


for idx in numbers:
    result += idx
result /= 3
print(result)
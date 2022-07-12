#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
#min() 함수 사용 금지

numbers = [0, 20, 100]

result = numbers[0]
for idx in numbers:
    if idx < result:
        result = idx
print(result)
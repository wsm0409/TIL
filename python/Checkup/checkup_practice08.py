#주어진 리스트 numbers에서 두 번째로 큰 수를 구하여 출력하시오.
#max() 함수 사용 금지

numbers = [0, 20, 100]

result = numbers[0]
resultwo = [0]
for idx in numbers:
    if idx > result:
        result = idx
    if result > idx:
        resultwo = idx
print(resultwo)
실패
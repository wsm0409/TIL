#주어진 리스트 numbers에서 두 번째로 큰 수를 구하여 출력하시오.
#max() 함수 사용 금지

numbers = [0, 20, 100, 40]

result = numbers[0]
resultwo = numbers[0]
for idx in numbers:
    if result < idx:
        resultwo = result
        result = idx
    elif resultwo < idx and idx < result:
        resultwo = idx
print(resultwo)

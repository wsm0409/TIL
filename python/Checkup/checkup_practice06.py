#주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
#max() 함수 사용 금지
#numbers = [0, 20 ,100 , -60, 50, 100]
#numbers = [0, 1, 0] 


numbers = [0, 120, 100]

result = numbers[0]
for idx in numbers:
    if idx > result:
        result=idx
print(result)
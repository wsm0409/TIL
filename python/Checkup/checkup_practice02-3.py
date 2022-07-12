#문자열 word의 길이를 출력하는 코드를 각각 작성하시오.

#len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

# input word = 'happy'

numbers =[0,20,100,120] 
max = 0
max2 = 0
for i in numbers:
    if i > max:
        max2 = max
        max = i
    elif max2 < i < max:
        max2 = i
print(max2)
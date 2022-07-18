#양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
#양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

number = int(input())
a = number
if 9 >= a > 0:
    print(1)
elif 99 >= a > 9:
    print(2)
elif 999 >= a > 99:
    print(3)
else:
    print('big')
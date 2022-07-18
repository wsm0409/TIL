
#점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

#평가 기준
#점수 범위 : 평가
# 90 ~ 100 : A
# 70 ~   89 : B
# 40 ~   69 : C
#   0 ~   39 : D
#로 평가되어야 한다.




a = int(input())
if 100 >= a >= 90:
    print('A')
elif 89 >= a >= 70:
    print('B')
elif 69 >= a >= 40:
    print('C')
elif 39 >= a >= 0:
    print ('D')
else:
    print('error')
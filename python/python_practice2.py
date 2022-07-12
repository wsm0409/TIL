#다음은 미세먼지 농도에 따른 등급일 때, dust 값에 따라 등급을 출력하는 조건식을 작성하시오.

num = int(input())
if num <= 30:
    print('좋음')
elif num <= 80:
    print('보통')
elif num  <= 150:
    print('나쁨')
elif num > 150:
    print('매우 나쁨')

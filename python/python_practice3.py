num = int(input())
if num <= 30:
    print('좋음')
elif num <= 80:
    print('보통')
elif num  <= 150:
    print('나쁨')
else:
    if num < 0:
        print('음수 값입니다')
    else:
        print('매우 나쁨')

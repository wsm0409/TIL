#실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.


a, b = input().split()
c = float(a) % float(b)
print(format(c, ".4f"))
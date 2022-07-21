#시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

T = int(input())
for i in range(1,T+1):
    a, b, c, d = map(int, (input().split()))
    R = a + c
    E = b + d
    if E > 60:
        E -= 60
        R += 1
        if R > 12:
            R -= 12
    elif R > 12:
        R -= 12
        if E > 60:
            E -= 60
            R += 1
    print(f'#{i}',R,E)
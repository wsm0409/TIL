# 백준 10995 별 찍기 -20   
#예제를 보고 규칙을 유추한 뒤 별을 찍어 보세요. https://www.acmicpc.net/problem/10995

N = int(input())

if N == 1:
    print('*')

else:
    for n in range(N):
        if n % 2 == 0:
            a = print('* ' * N)
        else:
            b = print(' *' * N)
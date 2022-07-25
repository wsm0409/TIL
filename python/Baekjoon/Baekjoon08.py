# 백준 2439 별 찍기 -2
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#하지만 오른쪽으로 정렬해야함
#1     *
#1    **
#1   ***
#1  ****
#1 *****

count = []
N = int(input())
for i in range(1, N+1):
    count += ('*')
    result = ''.join(map(str, count))
    print(result.rjust(N," "))
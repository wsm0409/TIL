#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

#(소수점 첫째 자리에서 반올림한 정수를 출력한다.) 


T = int(input())

for i in range(1, T+1):
    a, b, c, d, e, f, g, h, k, j = map(int, input().split())
    z = round((a + b + c + d + e + f + g + h + k + j)/10)
    print(f'#{i} {z}')
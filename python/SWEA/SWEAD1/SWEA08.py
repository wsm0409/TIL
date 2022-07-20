#알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
#N = int(input())
#A = chr(65)
#for i in range(1, N+1):
#    print(A, end=' ')
#    A = chr(65+i) 


n = input()

for i in (n):
    a = ord(i) - 64
    print(a, end=' ')

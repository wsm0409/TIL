# 백준 10953 A + B -6

T = int(input())
for i in range(1, T+1):
   A, B = map(int, (input().split(',')))
   if 10 > A > 0 or 10 > B >0:
      print(A + B)
   else:
      print(None)


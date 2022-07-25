# 백준 10950 A + B -3

T = int(input())
for i in range(1, T+1):
   A, B = map(int, (input().split()))
   if 10 > A > 0 or 10 > B >0:
      print(A + B)
   else:
      print(None)


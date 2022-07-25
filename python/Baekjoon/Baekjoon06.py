# 백준 11022 A + B - 8



T = int(input())
for i in range(1, T+1):
   A, B = map(int, (input().split()))
   if 10 > A > 0 or 10 > B >0:
      C = A + B
      print(f'Case #{i}: {A} + {B} = {C}')
   else:
      print(None)
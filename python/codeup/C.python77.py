

#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
b = 0
a = int(input())
for i in range(a + 1):
    if i % 2 == 0:
      b += i
print(b)
    
    
# 백준 X보다 작은 수 10871
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.


li = []
N ,X = map(int, (input().split()))
A = list(input().split())

for idx in A:
    if X > int(idx):
        li.append(idx)
print(' '.join(li))

            
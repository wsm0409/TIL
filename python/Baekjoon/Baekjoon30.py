# 백준 하얀 칸 1100
#체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

N, M = 8, 8
mat = []
count = 0
for i in range(N):
    for idx in range(M):
        mat.append([i,idx])
        if i+idx % 2 == 0:
            if mat == 'F':
                count += 1

box = []

for a in range(N):
    box.append(input().split())


print(mat)
print(box)
    
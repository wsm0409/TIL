#아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
#코드에서 오류를 찾아 원인을 적고, 수정하세요.


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    #55
    count += 1
    #10
a = f'{total / count: .1f}'
print(a)
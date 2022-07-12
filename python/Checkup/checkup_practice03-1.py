#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

#sum() 함수 사용 금지

#while문 이용
n = 0	
result = 0
user_input = int(input())

while n < user_input :
		n += 1
		result += n
print(result)


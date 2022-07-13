#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

#sum() 함수 사용 금지


#for문 이용
n=10	
result=0
for a in range(n+1):
    result += a
print(result)
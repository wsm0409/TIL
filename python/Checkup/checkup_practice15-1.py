#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
#a 가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지




word = input()
n = 0
for idx in word:
    if idx == 'a':  
        print(n)
        break
    else:
        n += 1 
if 'a' not in word:
    print(-1)

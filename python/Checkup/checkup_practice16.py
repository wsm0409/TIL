#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
#모음 : a, e, i, o, u 
#count() 사용 금지

result = 0
word = input()

for idx in word:
    if 'a' == idx or 'e' == idx or 'i' == idx or 'o' == idx or 'u' == idx:
        result += 1
        print(result)
#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지



word = input()
for idx in word:
    a = ord(idx) - 32
    b = chr(a)
    print(b)
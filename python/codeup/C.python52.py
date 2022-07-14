
#정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

a = int(input())
if a == 0:
    print('False')
else:
    print('True')




#bool을 사용하면 입력된 식이나 값을 평가해 0은 False으로 평가 그 외의 값은 True로 평가함
a = int(input())
print(bool(a))
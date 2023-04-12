'''
2023-04-12
김현탁
정수 2개와 연산자 1개를 입력받아서 
'''

# 1.변수 선언
i=int(input("첫번쨰 숫자를 입력해주세요:")) #첫번째 숫자 입력받기
operater=input("연산자를 입력해주세요: (+,-,*,/)") #연산자 입력받기
j=int(input("두번쨰 숫자를 입력해주세요"))#두번째 숫자 입력받기
# 2.
if operater== '+': #더하기
    print(i+j)
elif operater== '-': #뺴기
    print(i-j)
elif operater== '*': #곱하기
    print(i*j)
elif operater== '/': #나누기
    print(i/j)
else:               #그 이외에 오류일때
    print("연산자 오류")

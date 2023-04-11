'''
2023-04-11
김현탁
사칙연산
'''
i=int(input("첫번쨰 숫자를 입력해주세요:"))
operater=input("연산자를 입력해주세요: (+,-,*,/)")
j=int(input("두번쨰 숫자를 입력해주세요"))

if operater== '+':
    print(i+j)
elif operater== '-':
    print(i-j)
elif operater== '*':
    print(i*j)
elif operater== '/':
    print(i/j)
else:
    print("연산자 오류")

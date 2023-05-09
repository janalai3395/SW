'''
2023-05-09
김현탁
#문제 정의
    입력받은 숫자의 팩토리얼 구하기
#문제분석
    변수-정수(num),팩토리얼(fac)
#알고리즘
    1.변수 초기화
        num= int(input("팩토리얼 계산할 숫자 입력:"))
        fac=1
    2.프로그램 논리(반복for)    
        for i in range(num,0,-1):
            fac=fac*i
'''
num= int(input("팩토리얼 계산할 숫자 입력:"))
fac=1
for i in range(num,0,-1):
    fac=fac*i
print("%d의 팩토리얼 값은 :"%num,fac)
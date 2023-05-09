'''
2023-05-09
김현탁
#문제 정의
    1~100까지의 입력받은 숫자의 배수의 합계
#문제분석
    변수
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
        total=0
        i=0
    2.프로그램 논리(반복while)    
        while i<=100:
            i=i+1
            if i%num ==0:
                total=total+i
            else:
                continue
'''
num=int(input("배수 숫자 입력:"))
i=0
total=0
while i<=100: #선택조건
    i=i+1
    if i%num ==0: #선택조건(i가 num의 배수일때)
        total=total+i
    else: #i가 num의 배수가 아닐떄
        continue
print("1부터 100까지의{}의 배수의 합은:{}".format(num,total))

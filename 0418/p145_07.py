'''
2023-04-17
김현탁
두 정수 입력
#문제분석
    변수 i(첫번쨰숫자) j(두번쨰숫자)
    수식 i>j , i==j , i<j
#알고리즘
    1.변수선언
        i=int(input("첫번쨰 숫자 입력:")) #첫번쨰숫자를 정수로 입력
        j=int(input("두번째 숫자 입력:")) #두번쨰숫자를 정수로 입력
    2.논리(선택)
    if i>j:
        if j==0:
            print("에러")
        else:
            print(i/j)
    elif i<j:
        print(i+j)
    elif i==j:
        print(i*j)
    else:
        print("에러")
'''

i=int(input("첫번쨰 숫자 입력:")) #첫번쨰숫자를 정수로 입력
j=int(input("두번째 숫자 입력:")) #두번쨰숫자를 정수로 입력

if i>j: #첫번쨰 조건(나눗셈의 몫)
    if j==0: #j가 0일떄 예외처리
        print("0으로 나눌 수 없습니다.")
    else: #나눗셈하기
        print("{}//{}={}".format(i,j,i//j))
elif i<j: #두번쨰 조건 (합 출력)
    print("{}+{}={}".format(i,j,i+j))
elif i==j: #세번쨰 조건 (곱 출력)
    print("{}*{}={}".format(i,j,i*j))
else: #유비무환
    print("에러")

D=(i%j)
if j==0:
    print("{}는{}의 약수입니다.")
else:
    print("{}는{}의 약수가아닙니다.")
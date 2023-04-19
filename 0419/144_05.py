'''
2023-04-19
김현탁
144p05번
두 개의 숫자를 입력받아서 두번쨰 수가 첫 번쨰 수의 약수인지 구분하기.
#문제분석
    변수 i(첫번쨰숫자) j(두번쨰숫자)
    수식 D=(i%j)      j%i==0 (j는 i의 약수)
#알고리즘
    1.변수선언
        i=int(input("첫번쨰 숫자 입력:")) #첫번쨰숫자를 정수로 입력
        j=int(input("두번째 숫자 입력:")) #두번쨰숫자를 정수로 입력
    2.논리(선택)
        if j==0:
            print("{}는{}의 약수입니다.")
        else:
            print("{}는{}의 약수가아닙니다.")
'''

i=int(input("첫번쨰 정수를 입력하세요:")) #첫번쨰숫자를 정수로 입력
j=int(input("두번째 정수를 입력하세요:")) #두번쨰숫자를 정수로 입력
D=(i%j) #판별식

if j==0:
    print("0으로 나눌 수 없습니다.")
else:
    if D==0:
        print("{}는{}의 약수입니다.".format(j,i))
    else:
        print("{}는{}의 약수가아닙니다.".format(j,i))
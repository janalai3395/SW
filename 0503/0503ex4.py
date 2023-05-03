'''
2023-05-03
김현탁
#문제정의
    입력받은 단의 구구단 출력하기 (while 문으로)
#문제분석
    변수-단(dan),i
#알고리즘
    1.변수선언
        dan=int(input('구구단 단을 입력하시오'))
        i=1 #while 초기화 필요
    2.논리(while반복)
        (조건)while i<=9 :
        구구단 출력
'''
dan=int(input('구구단 단을 입력하시오'))
i=1 #while 초기화 필요
print('구구단',dan,'단') #제목 출력
while i<=9 : #조건
    print('{}x{}={}'.format(dan,i,dan*i))
    i=i+1 #1증가
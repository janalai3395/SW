'''
2023-04-19
김현탁
성별,키,몸무게를 입력 받아서 BMI 지수를 구하고 비만도 측정하기
#문제분석
    변수 sex=input("성별 입력('M' or 'm' 또는 'F' or 'f') :")
        height = float(input("키 입력(cm) : ")) / 100
        weight = float(input("키 입력(cm) : "))
    
    수식 
    avg = height * height * 22 #남자인경우
    avg = height * height * 21 #여자인경우
    bmi = weight/avg*100
#알고리즘
    1. 변수선언
        sex, height(실수), weight(실수)를 입력 받는다.
    2. 논리(내포된 선택)
        if 성별이 여자:
            avg계산
            if avg>=120:
                "비만"
            elif 110<=avg<=119:
                "과체중
            else
                "표준
        if 성별이 남자:
        else:
            성별 잘못 입력
'''

sex=input("성별 입력('M' or 'm' 또는 'F' or 'f' :)") #성별 입력 받기
height = float(input("키 입력(cm) : "))/100 #키 실수로 입력(M단위로 변환)
weight = float(input("몸무게 입력(kg) : ")) #몸무게 실수로 입력

if (sex=='M' or sex=='m'): #남자
    avg = height * height * 22
    bmi = weight/avg*100
    if 110 <=bmi<= 119:
        print("비만 체중")
    elif bmi>= 120 :
        print("과체중")
    else:
        print("정상 체중")
elif (sex=='F' or sex=='f' ): #여자
    avg = height * height * 21
    bmi = weight/avg*100
    if 110 <=bmi<= 119:
        print("비만 체중")
    elif bmi>= 120 :
        print("과체중")
    else:
        print("정상 체중")
else: #성별 입력이 잘못된 경우
    print("성별 입력이 잘못 되었습니다.")








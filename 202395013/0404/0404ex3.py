'''
2023.04.04
김현탁
표준입력(input())함수 연습
'''

name=input('이름을 입력해주세요:') #키보드로 이름을 입력받아서 name변수에 저장
score1= input('국어 점수:') #키보드로 국어 점수 입력받아서 score1 변수에 문자로 저장
score2= input('수학 점수:') #키보드로 수학 점수 입력받아서 score2 변수에 문자로 저장

print('{}의 점수합계는 {}이다.'.format(name,score1+score2))
print('\n') #한줄 띄우기

name1=input('이름을 입력해주세요:') #키보드로 이름을 입력받아서 name1변수에 저장
jumsu1= int(input('국어 점수:')) #키보드로 국어 점수 입력받아서 jumsu1 변수에 정수로 저장
jumsu2= int(input('수학 점수:')) #키보드로 수학 점수 입력받아서 jumsu2 변수에 정수로 저장

print('{}의 점수합계는 {}이다.'.format(name1,jumsu1+jumsu2))
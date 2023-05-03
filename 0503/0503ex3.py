'''
2023-05-03
김현탁
#문제정의
    1~입력받은 숫자까지의 합계 구하기
#문제분석
    변수 i #입력받을 정수
    sum #합계를 출력할값
#알고리즘
    1.변수선언
        i에 정수 입력
        sum=0
    2.논리(반복)
    (조건) for j in range (1,i+1)
    sum=sum+j
    print(sum)
'''
i=int(input('합계를 구할 숫자를 입력해주세요:'))
sum=0
for j in range(1,i+1):
    sum=sum+j
print('1~{}까지의 합계는:{}'.format(i,sum))

o=0
sum=0 #합계
while o<=i: #반복 조건
    sum=sum+o #합계 저장
    o=o+1 #i 1증가
print('1~{}까지의 합계는:{}'.format(i,sum))
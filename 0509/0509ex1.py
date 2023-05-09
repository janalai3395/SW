'''
2023-05-09
김현탁
#문제 정의
    두 숫자를 입력받아서 두 사이에 값을 더하는 프로그램
#문제분석
    변수-정수1(num1),정수2(num2),합계(sum),임시변수(temp)
#알고리즘
    1.변수선언 #변수초기화
    num1=int(input("첫번쨰 숫자를 입력해주세요:")) #첫번쨰 숫자 받기
    num2=int(input("두번쨰 숫자를 입력해주세요:")) #두번쨰 숫자 받기
    sum=0
    temp=0
    i=num1
    2.프로그램 논리(선택,반복)
        2-1.(선택조건) - 항상 num1<=num2
            if num1 > num2: #앞에 값이 더 클 떄 바꿔주는 코드
            temp=num1
            num1=num2
            num2=temp
        2-2.(반복) - num1~num2 까지의 1씩 증가하면서 더하기

'''

num1=int(input("첫번쨰 숫자를 입력해주세요:")) #첫번쨰 숫자 받기
num2=int(input("두번쨰 숫자를 입력해주세요:")) #두번쨰 숫자 받기
sum=0
temp=0
if num1 > num2: #앞에 값이 더 클 떄 바꿔주는 코드 (선택조건)
    temp=num1 #num1 값을 temp 에 저장
    num1=num2 #num2 값을 num1 에 저장
    num2=temp #temp 값을 num2 에 저장
i=num1
while i <= num2:
    sum=sum+i
    i+=1
print("{}~{}까지의 합계는:{}".format(num1,num2,sum))
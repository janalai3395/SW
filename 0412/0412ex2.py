'''
2023-04-12
김현탁
입력받은 두 수의 크기 비교
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수 선언
        num1,num2에 정수 입력    
    2.논리(선택)
        if num1 > num2 :
            (참) 더 큰수는 num1, 작은수는 num2 이다
        else:
            (거짓) 더 큰수는 num2, 작은수는 num1 이다
'''
num1 = int(input("첫 번쨰 숫자 입력"))
num2 = int(input("두 번쨰 숫자 입력"))
if num1 > num2 : #조건
    print("더 큰수는 {} 이고 작은수는 {} 입니다.".format(num1,num2)) #num1이 더 클떄
elif num1 < num2 : #조건
    print("더 큰수는 {} 이고 작은수는 {} 입니다.".format(num2,num1)) #num2가 더 클떄
elif num1 == num2 : #두 수가 같을떄
    print("두 수는 {}로써 같은 수입니다".format(num1))
else:
    print("에러")
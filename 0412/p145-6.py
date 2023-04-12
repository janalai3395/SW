'''
2023-04-12
김현탁
p145-6

#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수 선언
        -num1,num2에 정수 입력
    2.논리(if~elif~else)
        if (num1%2) == 0 and (num2%2) == 0:
            (조건1 참) print("{} + {} = {} ".format(num1,num2,num1+num2))
        elif (num1%2) == 0 and (num2%2) != 0:
            (조건2 참) print("두번쨰 정수를 짝수로 입력하세요.")
        elif (num1%2) != 0 and (num2%2) == 0:
            (조건3 참) print("첫번쨰 정수를 짝수로 입력하세요.")
        else:
            print("두 정수 모두를 짝수로 입력하세요.")
'''
num1 = int(input("첫 번쨰 숫자 입력"))
num2 = int(input("두 번쨰 숫자 입력"))
if (num1%2) == 0 and (num2%2) == 0:
    print("{} + {} = {} ".format(num1,num2,num1+num2))
elif (num1%2) == 0 and (num2%2) != 0:
    print("두번쨰 정수를 짝수로 입력하세요.")
elif (num1%2) != 0 and (num2%2) == 0:
    print("첫번쨰 정수를 짝수로 입력하세요.")
else:
    print("두 정수 모두를 짝수로 입력하세요.")
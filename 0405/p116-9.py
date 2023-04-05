'''
2023.04.05
김현탁
홍길동의 월급 수령액 구하기 p116-9
'''

Base_Salary=int(input('기본 본봉을 입력해주세요:')) #본봉을 정수로 입력받는코드
Bonus=int(input('보너스 를 입력해주세요:')) #보너스를 정수로 입력받는코드
Tax_Rate = 0.2 #세율

Total_Salary = Base_Salary + Bonus #총액 구하는 함수
Taxes = Total_Salary * Tax_Rate #세금
Take_Home_Pay = Total_Salary - Taxes #실수령액

print("본봉이 {}이고, 수당이 {}이고, 세율이{}일떄 실수령액은{}이다.".format(Base_Salary,Bonus,Tax_Rate,Take_Home_Pay)) #실수령액을 출력하는 함수

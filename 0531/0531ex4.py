'''
2023-05-31
김현탁
#문제정의
    각 요소가 튜플에 몇 번 나타났는지 출력하는 프로그램
#문제분석
    변수-리스트 num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
    num_list=[] #빈 리스트
#알고리즘
    1.튜플 정의
    2.빈 리스트 생성
    3.반복(각 리스트의 요소가 몇번 나타났는지 찾음)
        for i in range(len(num)): #튜플 길이 만큼 반복
            if num[i] not in num_list:#리스트에 없는 경우
                num_list.append(num[i]) #리스트에 추가
                print(num[i],"개수 : ",num.count(num[i]))#갯수 출력
'''

num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
num_list=[]

print("생성된 튜플:",num)

for i in range(len(num)): #튜플 길이 만큼 반복
    if num[i] not in num_list:#리스트에 없는 경우
        num_list.append(num[i]) #리스트에 추가
        print(num[i],"개수 : ",num.count(num[i]))#갯수 출력


'''
2023-05-16
김현탁
파일 입출력
'''
ft=open("c:/data/test.txt","w") #파일 객체 ft 생성(쓰기)

for i in range(1,11): #10번 반복
    ft.write("%d번쨰 줄입니다.\n"%i) #ft에 i 출력

ft.close #파일 종료

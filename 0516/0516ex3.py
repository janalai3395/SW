'''
2023-05-16
김현탁
파일 입출력 - 읽기
'''
f=open("c:/data/test.txt","r") #파일 객체 생성(읽기)

txts=f.read() #파일 전체 내용을 txts에 하나의 문자열로 반환

print(txts) #읽은 내용 출력

f.close() #파일 종료
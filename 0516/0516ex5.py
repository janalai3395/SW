'''
2023-05-16
김현탁
파일 입출력 - writelines() ->리스트나 튜플 같은 자료형을 파일에 저장
                            ->리스트나 튜플의 자료형은 문자열 이여야 한다.
            -write() ->문자열 만 파일에 출력
'''

#문자열 리스트
L1=['충청남도','충청북도\n','전라남도','전라북도\n','경상남도','경상북도\n']

#정수형 리스트
L2=[1,2,3,4,5]

#with 
with open("c:/data/linetest.txt","w") as f:

    f.writelines(L1) #L1리스트 내용을 파일에 출력

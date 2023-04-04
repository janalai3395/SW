'''
2023.04.04
김현탁
표준출력(print) format()연습
'''

print('이름은 {}이고 나이는 {}입니다.'.format('Hyun Tak Kim',25))
print('이름 {name} 나이{age}, 주소{adress}'.format(adress='Busan',name='Hyun Tak Kim',age='25'))
print('The Lucky Number is ({:14})'.format(7777)) #숫자는 기본 오른쪽 정렬
print('The Lucky Number is ({:<14})'.format(7777)) #숫자 왼쪽 정렬

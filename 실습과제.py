'''
문자를 입력받고 원본 문자를 반전시켜서 반대문자열로 출력하는 코드를 작성해보자
파이썬 -> 썬이파
'''

str_1 = str(input('문자 입력 : '))
reversed_value = str_1[::-1]
print('반대 문자열 : ', reversed_value)

'''
문자 입력 : 파이썬
반대 문자열 :  썬이파
'''

str_2 = ['a', 'b', 'c']
str_2.reverse()
print(str_2) #['c', 'b', 'a']
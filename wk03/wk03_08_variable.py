# wk03_08_variable.py

print("변수: 변수란?")
#
# 변수는 자료(값)을 저장하는 공간이다.
#
a = [1, 2, 3]
id(a)  # a 변수가 가리키는 메모리의 주소
# list
a = [1, 2, 3] #같은 리스트라도 저장되는 주소값은 달라진다
id(a)  
b = a #값을 대입하면 같은 주소값을 공유한다
id(a), id(b) 
a is b
a[1] = 4
a, b
a is b
b = [1, 2, 3]
id(b)
a is b
#
# b 변수를 생성할 때 a 변수의 값을 가져오면서
# a와는 다른 주소를 가리키도록 만들수는 없을까?
# 다음 2가지 방법이 있다.
#
# 1. [:] 이용
# a와 b의 주소가 따로설정된다. [1,4,3],[1,2,3]
a = [1, 2, 3] 
b = a[:]
a[1] = 4
a, b
#
# 2. copy 모듈 이용
#
a = [1, 2, 3]
# from copy import copy
b = copy(a)

b is a, a is b

#
# 변수를 만드는 여러 가지 방법
#
a, b = ("python", "life") #튜플은 앞에 소괄호 안넣어도된다.
a
b
a, b

[a, b] = ["python", "life"] #리스트는 앞에 대괄호 넣어야함.
a
b

a = 3
b = 5
a, b = b, a
a
b

#
#
"""
Author: redwoods
파이썬 코드: wk03_08_variable.py
"""

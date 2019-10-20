# wk03_04_tuple.py

print("튜플: tuple 이란?")
# 리스트는 [ ] 대괄호, 튜플은 ( ) 소괄호. 딕셔너리는 {} 중괄호사용
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

even = (2, 4, 6, 8)
# 여러 가지 튜플
t1 = ()   # 튜플 초기화
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# t2 = (1,)처럼 단지 1개의 요소만을 가질 때는 요소 뒤에
# 콤마(,)를 반드시 붙여야 한다는 것과
# t4 = 1, 2, 3처럼 괄호( )를 생략해도 무방하다.
#####################################################
#
# 튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?
#
# 1. 튜플 요솟값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
del t1[0]  # Error
#
# 2. 튜플 요솟값을 변경하려 할 때
#
t1[0] = 'c'   # TypeError
#
#
print("튜플: 사용방법")
#
# 인덱싱하기
#
t1 = (1, 2, 'a', 'b')
t1[0]
t1[3]
#
# 슬라이싱하기
#
t1 = (1, 2, 'a', 'b')
t1[1:]
t1[2:-1]  # ('a',)
t1[2:]
#
# 튜플 더하기
#
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2
#
# 튜플 곱하기
#
t2 = (3, 4)
id(t2)
t2 * 3
id(t2)
t2 = t2 * 3
id(t2)
#
# 튜플 길이 구하기
#
t1 = (1, 2, 'a', 'b')
len(t1)
#
#
"""
Author: redwoods
파이썬 코드: wk03_04_tuple.py
"""

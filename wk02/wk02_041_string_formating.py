# wk02_04_string_formating.py

print("문자열: 포매팅이란?")
# 1. 숫자 바로 대입
"I eat %d apples." % 3

# 2. 문자열 바로 대입
"I eat %s apples." % "five"

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % number #, day   # Error // 2개의 출력형태 각각 넣어줘야함
"I ate %d apples. so I was sick for %s days." % (number, day)
# 소괄호 안에 콤마(,)로 구분하여 각각의 값을 넣어 준다.

print("문자열: 포맷 코드")
# %d, %s, %c, %f, %o, %x, %% //정수,문자열,문자하나,실수,8진수,16진수,%기호
# %s, 묵시적 형변환
"I have %s apples" % 3
"rate is %s" % 3.234

"Error is %d%." % 98 // %출력은 %% 넣어줘야함
"Error is %d%%." % 98

###############################################-p60
print("문자열: 포맷 코드와 숫자 함께 사용하기")
# 1. 정렬과 공백
"%10s" % "hi"
"%-10sjane." % 'hi'
# 2. 소수점 표현하기
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234

print("문자열: format 함수를 사용한 포매팅")
# 1. 숫자 바로 대입하기 
"I eat {0} apples".format(3)
"I eat {0} {1} apples".format(3, 4)  # format함수 사용시 인덱스 순서 지정  

# 2. 문자열 바로 대입하기
"I eat {0} apples".format("five")
"I eat {0} apples from {1} boxes".format("five", "3")

# 3. 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)
"I eat {0} apples".format(number+1)

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
#
######################################
# 왼쪽 정렬/ 오른쪽 정렬
"{0:<10}".format("hi")
"{0:>10}".format("hi")
# 가운데 정렬
"{0:^10}".format("hi")
# 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")
# 도전하기
"{0:<10}{1:>10}".format("hi",'hcit') # 0=첫번째 문자열, 1=두번째 문자열

#########################################

# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)
# { 또는 } 문자 표현하기
"{{ and }}".format() #중괄호 나타낼 때, %%처럼 두개 사용

##########################
##### f 문자열 포매팅 #####
##### .format() 대체
##########################
print("문자열: f 문자열 포매팅")
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

age = 30
f'나는 내년이면 {age+1}살이 된다.' # f가 format함수 대체

# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용 // key value 한쌍 자료형
d = {'name': '홍길동', 'age': 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# 정렬
f'{"hi":<10}'  # 왼쪽 정렬
f'{"hi":>10}'  # 오른쪽 정렬
f'{"hi":^10}'  # 가운데 정렬
# 공백 채우기
y = 3.42134234
f'{y:0.4f}'  # 소수점 4자리까지만 표현
f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
# { } 문자를 표시
f'{{ and }}'

##############################################
print("문자열: 관련 내장 함수들")
# 문자 개수 세기(count)
a = "hobby"
a.count('b') # a에 b가 몇개 들어있는지
# 위치 알려주기1(find)
a = "Python is the best choice"
a.find('b')
a.find('k')  # -1 반환
# 위치 알려주기2(index)
a = "Life is too short"
a.index('t')
a.index('k') # error 반환

# 문자열 삽입(join)
",".join('abcd')
",".join(['a', 'b', 'c', 'd'])
# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()
# 대문자를 소문자로 바꾸기(lower)
a = "IoT"
a.lower()
# 왼쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()
# 오른쪽 공백 지우기(rstrip)
a.rstrip()
# 양쪽 공백 지우기(strip)
a.strip()
# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg") # (바뀌게 될 문자열, 바꿀 문자열) 치환

# 문자열 나누기(split) -> 리스트로 변환하여 반환  #중요!!
a = "Life is too short"
a.split()
b = "a:b:c:d"
b.split(':') # :을 기준으로 구분

#### 도전하기 ##### 단답 출제확률
# format 함수 또는 f 문자열 포매팅을 이용해서 '!!!python!!!' 문자열을 출력해보시오.
"{0:!^12}".format('python')
f'{"python":!^12}'


"""
Author: redwoods
파이썬 코드: wk02_04_string_formatting.py
"""
#wk_03_01_list
print("리스트 : list란?")
a =[] # list 초기화
b=[1,2,3]
c=['Life', 'is', 'too', 'short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']] #list 안의 list 2차원 배열
a=list() # list객체 생성자,(초기화)

#리스트의 인덱싱
print("리스트 : 리스트의 인덱싱과 슬라이싱")
a = [1, 2, 3]
a
a[0]
a[0]+ a[2]
a[-1] # 리스트 a의 마지막 요소값
a = [1,2,3,['a','b','c']]

#삼중 리스트 인덱싱 
a = [1, 2, ['a','b',['Life','is']]] # 3차원
a[2][2][0] 

# 리스트 슬라이싱
a = [1,2,3,4,5]
a[0:2]
a="12345"
a[0:2]
a[:2]
a[0:4:2] # a[start:end:step]

# 리스트 더하기
a = [1,2,3]
b = [4,5,6]
a + b 

# 리스트 반복하기
a = [1,2,3]
a * 3

# 리스트 길이 구하기
a = [1,2,3]
len(a)

print(a[2] + "hi")
str(a[2])+"hi"

#del 함수로 리스트 요소 삭제
a=[1,2,3]
del a[1]
a

# 리스트에 요소 추가 (append)
a = [1,2,3]
a.append(4)
a

# 리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
a

# 리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
a

# 리스트 위치 반환(index)
a = [1,2,3]
a.index(3)
a.index(1)

# 리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4) # 0번째 자리에 4 삽입
a

# 리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
a.remove(3) #첫 번째로 나오는 x 삭제
a

# 리스트 요소 끄집어내기(pop)
a=[1,2,3]
a.pop()
a



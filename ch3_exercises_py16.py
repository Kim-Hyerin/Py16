## ch3_exercises_py16

## Q1.
> 다음 코드의 결괏값은 무엇일까?

```
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

```

# [Q1] Code  
##결괏값으로 shirt 가 출력된다.

##첫 번째 조건: "wife"라는 단어는 a 문자열에 없으므로 거짓이다.
##두 번째 조건: "python"이라는 단어는 a 문자열에 있지만 "you" 역시 a 문자열에 있으므로 거짓이다.
##세 번째 조건: "shirt"라는 단어가 a 문자열에 없으므로 참이다.
##네 번째 조건: "need"라는 단어가 a 문자열에 있으므로 참이다.
##가장 먼저 참이 되는 것이 세 번째 조건이므로 "shirt"가 출력된다.



## Q2.
> while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.


# [Q2-1] Code
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

# [Q2-2] Code
num = 0
sum = 0
while num < 1000:
    num = num +1
    if num % 3  == 0: 
        sum= sum+num

print(sum)

## Q3.
> while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

```
*
**
***
****
*****

```


# [Q3-1] Code
i = 0
while True:
    i += 1
    if i > 5: break
    print ('*' * i)

# [Q3-2] Code
a = 0
while a < 5:
    a = a +1    
    print('*' * a) 

## Q4.
> for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
- 단순 for문 사용
- 리스트 내포 사용

# [Q4-1] Code
 for i in range(1, 101):
    print(i)

# [Q4-2] Code
a = [i + 1 for i in range(100)]
print(a)

## Q5.
> A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

- [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

- for문을 사용하여 A 학급의 평균 점수를 구해 보자.

# [Q5] Code

a = [70,60,55,75,95,90,80,80,85,100]
total = 0

for score in a:
  total += score
  
aver = total / len(a)
print(aver)

## Q6.
> 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
```

- 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

# [Q6] Code

numbers = [1,2,3,4,5,6,7,8,9]
result = [n * 2 for n in numbers if n%2==1]
print(result)

## Q7.
> ## [Challenge] 응용 코드 : 평균 성적을 구하시오.
```
subjects = ['파이썬', '영어', '수학', '물리']
scores = [91, 67, 88, 75]
```

- 평균 성적을 세가지 이상의 방법으로 구하시오.

# [Q7] Code-1

subscores = {'파이썬':91,'영어':67, '수학':88, '물리':75}
average = sum(subscores.values()) / len(subscores)
print(average)

# [Q7] Code-2

def aver(파이썬,영어,수학,물리):
  return (파이썬+영어+수학+물리)/4
print(aver(91,67,88,75))

## 코딩 연습 결과를 github에 올리기
> 완성된 ipython 노트북 파일을 각자의 github에 올리시오.

- github 계정 만들기 (계정이 없는 학생)
    1. github에 sign up (Google gmail 계정을 이용해서 만드시오.)
- github에 노트 올리기
    2. github에 각자의 id로 repo를 만드시오. (한번 만들면 계속 재사용)
    3. github repo에 연습결과 노트를 올리시오.
        - 제출노트: ch3_exercises_id.ipynb

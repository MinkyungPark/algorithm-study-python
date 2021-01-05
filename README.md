# 1.
- **codeup 기초 100제**
# 2.
- **백준온라인 저지**
- 단계별, 유형별 문제
- 배열, 문자열, 정렬, 브루트포스, 재귀, 백트래킹, 동적계획법, dfs/bfs
# 3.
- **프로그래머스**
- 코딩테스트 고득점 kit
- 유형별 4~7개 풀면서 자주 나오는 유형을 익히고
# 4.
- **프로그래머스 스킬체크**
- 주어진 시간 내 2문제
- 레벨3
### 참고
- 완전탐색, 시뮬레이션 먼저(완전탐색을 재귀나 백트래킹으로 하는 거)
- 그 다음 그래프(위상정렬, 다익스트라 등등 포함..)
- 최소신장트리(유니온파인드 등..)
- 심화문제(스택으로 라인스위핑)
- 코테에 dp가 나오면 완죠니 어렵다.

<br>

---------------------------------------------------------------
---------------------------------------------------------------

<br>

## ○ 완전탐색(BP - Brute Force)
- 말 그대로 모든 경우의 수를 다 해보는 것.
- 정확하지만 시간이 최대, 효율성이 떨어진다.
### 푸는 방법
- 백준 2309, 1476, 14500, 1966,2231
- 모든순열 구하기 10974, 10819, 2098 유명한 NP문제들 dfs로도 풀 수 있다.
case1. for,if문 - brute force 처음부터 끝까지 탐색
case2. 순열, 조합 사용 (O(N!))
case3. 재귀함수
case4. 비트마스크
case5. 백트래킹
case6. bfs
### 순열
- 서로다른 n개의 원소에서 r개를 중복 허용하지 않고 순서대로 늘어놓은 것. nPr
- 파이썬의 itertools.permutations, .combinations 사용하면 쉽게 풀 수 있다.
### 백트래킹
- 조합 알고리즘 문제에 대해 모든 가능한 해를 나열하는 것
- 모든 조합의 수를 살펴보는 테크닉이다. 단, 조건이 만족할 때만.
- DFS,BFS + 조건 ---> 가지치기, 백준 1697

<br>

## ○ DFS, BFS
### BFS
#### QUEUE
- 인접 노드 중 방문하지 않은 노드를 큐에 넣을 때 set타입을 사용하면 쉽게구현할 수 있다.
- **set**은 집합 자료형 : 중복을 허용X, 순서가 없다, 따라서 인덱싱이X
- 파이썬의 큐 구현, 보통 .append, .pop을 이용하나 pop의 시간복잡도는 O(N)이다.
- collections의 dequeue를 사용하면 시간을 절약할 수 있다.
- **dequeue**는 double-ended queue임, 양방향에서 데이터를 처리할 수 있는 자료구조.
- deque의 메소드 : append, appendleft, pop, popleft, extend, extendleft
stack = [], statck.pop(), stack.append() <br>
q = deque([start]), q.popleft(), q.append() <br>


<br>

## ○ Simulation
- 문제에서 주어진 처리를 수행하기만 하면 되는 간단한 내용
- 푸는 방법 탐색
- 완전 탐색과의 차이 : 시뮬은 수행해야 하는 과정이 모두 나와있고 완전탐색은 모든 패턴을 조사해야 하는 것
- 둘을 명확히 구분할 필요는 없다.

<br>
<br>
<br>

---------------------------------------------------------------
---------------------------------------------------------------

<br>

# ○ 파이썬을 파이썬 답게 쓰자
### - enumerate()
- 인덱스와 값 둘 다 사용하고 싶을 때 for idx, value in lis:
<br>

### - dictionary 빠르고 좋다. 많이 쓰자
- .get(), del dic[key], .clear(), 'abc' in dic;
- key는 중복되지 않으므로 대치됨. key에 리스트는 쓸 수 없으나 튜플은 가능
- items는 둘다 for key, value in dict.items(), items 는 key-value 쌍이 튜플로 구성된 리스트가 리턴.
- 정렬은 sort가 아닌, sorted로 수행 <br>
: sorted(dict.items()) // 키로 정렬 <br>
: sorted(dict.items(), reverse=True) // 내림차순 <br>
: sorted(dict.items(), key=operator.itemgetter(0)) // 키로 정렬 <br>
: sorted(dict.items(), key=operator.itemgetter(1)) // 밸류로 정렬 <br>
=> sorted(dict.items())하면 튜플로 반환되고, [(key,value),(key,value)..] 여기서 0은 key 1은 value <br>
: sorted(dict.items(), key=lambda item:len(item[0])) // 키의 길이 기준으로 정렬 <br>
: sorted(dict.items(), key=lambda item:item[1]) // 밸류로 정렬
- keys()는 키만, values()는 값만
- dictionary min, max, sorted가능하지만 append,pop,remove,insert,sort등 리스트의 함수 수행안됨 <br>
=> setdefault(k,v), update(k,v) 메소드를 이용.


<br>

### - 포랑 이프문 여러줄로 쓰지말자
- result = [key for key, value in score.items() if value == highest]
- list(map(''.join, itertools.permutations(lis, 3)))
- list(set(map(''.join, itertools.permutations(lis))))
- (' '.join(list(map(str, dfs(graph, v)))))
<br>

### - zip()
- 김밥자르는거임. List를 여러개를 슬라이싱할 때
- for a, b in zip(A,B):
<br>

### - collections.Counter
- 해쉬를 생성할때
- value가 큰 순, 즉 개수가 많은 수로 저장되어있다. 
A = {'a','b','c','a','a','b'} <br>
dict = {'a':3,'b':2,'c':1} 만들려면, dict={} 생성하고 for문돌려서 value+=1 해주어야했는데 <br>
Counter를 사용하면 한줄로 가능.....<br>
ex1)<br>
Counter('aaaabbc')  # {'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}<br>
ex2)<br>
cntr = Counter(lis) <br>
hash = Counter([val for val in A])  # {'a':3,'b':2,'c':1} <br>
: hash처럼 사용하면 된다. .keys(), .values(), .items()

<br>

### - 출력과 입력
#### 출력
- print의 인자 seq= 는 구분자(기본값이 공백), end= 는 마지막 문자열을 출력하고 출력할 문자(기본값이 줄바꿈)
- print('나의 이름은 "%s"이고, 나의 나이는 %d살 이다.' % ('박이구', 2))
##### .format()
- 형식에 맞추어 출력할 때
- print('나의 이름은 {}이다.'.format('박이구'))
- print('나의 이름은 {1}이고, 나의 나이는 {0}살 이다.'.format(2, '박이구'))
- print('삼삼칠 박수 :  {0}!!! {0}!!! {1}!!! '.format('짝'*3,'짝'*7))
- print('나이는 {age}세이고 성별은 {gender}입니다. 나의 이름은 "{name}"입니다.'.format(name='한사람',age=33,gender='남성'))
<br>

### 리스트, 딕셔너리
#### 딕셔너리
##### 삭제
- del dict[key] // 반환 X
- pop = dictp.pop(key) // 값 반환
- dict.clear()
##### 관련함수

<br>

#### 리스트
##### 삭제
- del lis[idx] // 반환 X
- pop = lis.pop(idx) // 값 반환
- pop = list.pop() // 제일 뒤의 값 삭제 및 반환
- lis.remove(value)
- lis.clear()
##### 관련함수
- sum(list) -> 리스트의 합
- if 리스트: -> 리스트에 요소가 있으면 즉, 길이가 1이상이면 실행
- any(), all() <br>
if any(cur[1] < q[1] for q in queue): ~ <br>
any([False, False, True]) # True <br>
any(letter == 't' for letter in 'monty') # True

<br>

##### if item in list / if item in dict
- if 'abcd' in ['abcd','ab','a'] = True
- if 'abcd' in {'abcd':0,'ab':0,'c':0} = True

<br>

- **길이와 정렬**
- {:길이} : 출력할 데이터의 길이를 지정합니다. 문자열(왼쪽 정렬), 숫자(오른쪽 정렬)
- {:<길이} : 왼쪽 정렬
- {:>길이} : 오른쪽 정렬
- {:^길이} : 가운데 정렬
- **Example 1* <br>
 print('Python is [{:>15}]'.format('good')) <br>
 Python is [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;good] <br>
- **Example 2* <br>
 for x in range(1, 4): <br>
    print('[{0:2d}] [{1:3d}] [{2:4d}]'.format(x, x*x, x*x*x)) <br>
 0은 x, 1은 x*x, 2는 x*x*x 이고 2칸자리, 3칸자리, 4칸자리를 의미 <br>
 [&nbsp;1] [&nbsp;&nbsp;1] [&nbsp;&nbsp;&nbsp;1] <br> [&nbsp;2] [&nbsp;&nbsp;4] [&nbsp;&nbsp;&nbsp;8] <br> [&nbsp;3] [&nbsp;&nbsp;9] [&nbsp;&nbsp;27] <br>
- 기타 더 있음 참고하기 : https://wikidocs.net/20403

<br>

### Lambda
#### lambda 인자 : 표현식
- 익명함수 <br>
result = lambda x,y:x+y <br>
reault(1,2) # 3 <br>
(lambda x,y:x+y)(1,2) <br>

#### list(map(함수 , 리스트))
- 리스트 원소를 각각 꺼내 함수에 적용 시킨 뒤 새로운 리스트 반환 <br>
list(map(lambda x: x ** 2, range(5)))  # [0, 1, 4, 9, 16] <br>

#### reduce(함수, 순서형자료)
- 순서형자료(문자열, 튜플, 리스트) 의 각 원소를 함수에 누적 <br>
from functools import reduce <br>
reduce(lambda x,y:x+y, [1,2,3,4]) # 10 <br>
reduce(lambda x,y:y+x, 'abcde') # edcba

#### filter(함수, 리스트)
- 리스트 요소들 함수에 맞는 조건만 새로운 리스트에 <br>
filter(lambda x:x<5, range(10)) # [0,1,2,3,4]

<br>

### Math
#### import math
- math.abs() 절대값
- math.ceil()
- math.round()
- math.floor()

<br>

---------------------------------------------------------------
---------------------------------------------------------------

<br>

## 런타임에러
- ideone.com
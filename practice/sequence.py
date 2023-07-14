#이번장에서는 파이썬 내장 시퀀스 데이터타입을 보자, 사실상 tensor이전이나 numpy이전에 많이 사용되고 기본이지만 할때마다 까먹거나 헷갈려서 다시 찾아보는 경우가 있는것같다.
#이번 기회로 까먹지 않도록 기억할 수 있었으면 좋겠다.

#시퀀스 타입은 다음과 같은 속성을 가진다. 
#맴버십 연산 : in keyword이용
#크기 함수 
#슬라이싱 속성
#반복성 이며 파이썬에서는 문자열 튜플 리스트 바이트배열, 바이트 등 5개의 내장 시퀀스타입이 있다.
l = []
print(type(l))
s = ''
print(type(s))
t = ()
print(type(t))
ba = bytearray(b'')
print(type(ba))
b = bytes([])
print(type(b))

#우선 숫자와 다르게 몇개는 가변성을 가지고 있다. 튜플, 문자열, 바이트는 불변객체이지만 리스트와 바이트는 가변 객체타입이다. 일반적으로 불변객체 타입은 가변 객체 타입보다 효율적이다.
#파이썬의 모든 변수는 객체 참조이므로 가변객체를 복사할 때는 매우 주의해야한다. a=b라고 해도 a는 실제 b가 가리키는 곳을 가리킨다. 즉 a라는 것이 새롭게 만들어진게 아닌, b를 참조하고 있는 것이다.
#따라서 깊은 복사(deep copy)를 이해해야한다. (이것때문에 저번에 한번 된통 당한적있다.)
mylist = [1,2,3,4]
new_list = mylist[:] #깊은 복사됨
new_list2 = list(mylist) #깊은 복사됨
print(new_list)
print(new_list2)

#set에서 깊은 복사 예시는 다음과 같다
people = {'a','b','c'}

slayers = people.copy()
slayers.discard('c')
slayers.remove('a')
print(slayers)
print(people)
#깊은 복사가 진행되었기 때문에 slayers에서 삭제해도 people에는 영향이 없다.
#딕셔너리에서 깊은 복사는 다음과 같다.
mydict = {'a':'b'}
new_my_dict = mydict.copy()
#기타 객체의 깊은 복사를 원하게된다면 copy모듈을 이용할 수 있다.
import copy
myobj = 'str객체'
new_obj = copy.copy(myobj) # 얕은 복사, 같은곳을 가르키고있다.
new_obj2 = copy.deepcopy(myobj) # 깊은 복사.


#슬라이싱 연산자 파이썬 시퀀스 타입에서 슬라이싱 연산자의 구문은 다음과 같다.
# seq[시작], seq[시작:끝], seq[시작:끝:step] 만약에 오른쪽 끝에서 부터 읽고싶다면 인덱스를 음수로 표현하면 된다.

word1 = 'asdf'
print(word1[-1])
print(word1[-2:]) #뒤에 두번째부터~
print(word1[:-2]) #뒤에 두번째까지~

#문자열 -> 파이썬은 불변의str타입을 이용하여서 문자열을 표현한다.
#파이썬의 모든 객체에는 두가지 출력형식이 있다. 문자열(string) 형식은 사람을 위해서 설계되었고, 표현(representational) 형식은 파이썬 인터프리터에서 사용하는 문자열로 보통 디버깅할때 사용됨.

#문자열에 존재하는 여러가지 메서드들을 알아보자
#join()메서드 -> A.join(b)는 리스트 b에 있는 모든 문자열을 하나의 단일 문자열 A로 결합한다. 문자열을 연결할때는 +를 사용해도되지만, 많은양의 문자열이 있다면 비효율적일 수 있다.
name = ['a','b','c']
print(' '.join(name)) # A를 중간에 기준으로 만들수 있다.
print(''.join(name))
print(''.join(reversed(name))) #list에 reversed를 넣어줘서 반대로 출력될 수 있게한다.

#ljust(),rjust()는 A.ljust(width,fillchar)이고 l은 문자열A의 오른쪽에 width만큼의 문자를 채우고, r은 문자열의 왼쪽에 채워준다.
name = 'oh'
print(name.ljust(50,'-'))
print(name.rjust(50,'-'))

#format()은 문자열 A에 변수를 추가하거나, 형식화하는데 사용된다.
print('{} {}'.format('hello','world!'))
print('{age} {name}'.format(age=26,name='hyunskki'))

#문자열 언패킹(mapping unpacking)의 연산자는 **이고 이를 사용하면 함수로 전달하기에 적합한 key-value 딕셔너리가 만들어진다.
#해당 예제에서 local메서드는 언패킹해서 딕셔너리로 반환해준다
name = 'hyunskki'
age = 26
print('{age}:{name}'.format(**locals()))

#splitlines() 메서드 A.splitlines()는 문자열A에 대해서 줄바꿈 문자를 기준으로 분리환 결과를 문자열 리스트로 반환한다.
names = '로미오\n줄리엣'
print(names.splitlines())
#split()메서드는 A.split(t,n)이고 문자열A에서 t를 기준으로 n번만큼 분리한 문자열을 반환한다 n을 지정하지 않으면 t로 최대한 분리한다.
names = 'a*bbb-cc*16'
fields = names.split('*')
print(fields)
fields2 = names.split('-')
print(fields2)

#stip()은 A.stip(B)으로 사용하고 문자열 A 앞뒤의 문자열 B를 제거한다. 인수 B가 없으면 공백문자를 제거한다.
names = 'romeo & july999'
print(names.strip('999'))

#swapcase()메서드 A.swapcase()는 문자열 A에서 대소문자를 반전한 문자열의 복사본을 반환함
names = 'Buffy and Faith'
print(names.swapcase())
#비슷하게 capitalize()는 문자열 첫 글자를 대문자로, lower()메서드는 전체 문자열을 소문자로 upper는 대문자로 변환해준다.
print(names.lower())
print(names.upper())

#index(), find()메서드는 문자열 안에서 또 다른 문자열의 인덱스 위치를 찾는다. A.index(sub,start,end)는 문자열A에서 부분 문자열 sub의 인덱스위치를 반환한다. A.find(sub,start,end)는 문자열 A에서 부분 문자열 sub의 위치를 반환한다. 둘의 차이점은 없을때 index는 value error를 발생시키고, find는 -1을 반환해준다.
print(names.index('y'))
print(names.find('y'))
print(names.find('z'))

#replace 메서드 A.replace(old,new,maxreplace)는 문자열 old를 대체문자열 new로 변환해주고, maxreplace만큼 변경한 문자열의 복사본을 반환한다. 즉 maxreplace는 제한횟수가 되는것
names = 'buffy is buffy is buffy'
print(names.replace('buffy','hyunskki',2)) # 2라서 2번만 바꿔줌 

#count()메서드는 A.count(sub,start,end)로 start end범위 내에서 문자열 sub가 얼마나 많이 나왔나 세어준다.
print(names.count('buffy',0,-1))
#지정을 안해준다면 전체에서 세어서 반환해준다.
print(names.count('buffy'))

#f-string 메서드는 3.6버전 이상에서부터 사용가능하고, 문자열 앞에 f를 붙여주면 사용할 수 있다. 기존의 %나 .format보다 간결하고 속도도 빠르다고 한다.
name = 'hyunskki'
print(f'그의 이름은 {name!r}') #여기에서 하나 더 !r을 붙이면 출력시 따옴표로 감쌀 수 있음
print(f'그의 이름은 {name}')

#튜플(tuple)은 쉼표로 구분된 값으로 이루어지는 불변 시퀀스타입이다. 불변이라서 변환하고 싶다면 dict같은걸로 변환하고 바꿔줘야한다.
t1 = 1234,'hello'
print(t1[0])
t2 = t1,(1,2,3,4) #중첩이 가능하다.
print(t2)
#문자열에 각 위치에 단일 문자가 있는 것처럼, 튜플은 각위치에 객체 참조를 같는다. 
t1 = 'he','she'
print(len(t1))

#튜플 메서드 A.count(x)는 튜플 A에 담긴 항목 x의 개수를 반환한다.
t = 1,5,7,4,4
print(t.count(4)) # 2
#index는 위치를 반환해줌
print(t.index(5))

#튜플 언패킹. 파이썬에서 모든 반복 가능한 객체는 시퀀스 언패킹 연산자 *를 이용하여 언패킹할 수 있다. 변수를 할당하는 문장에서 왼쪽에 두개 이상의 변수를 사용하고, 한 변수앞에 *가 붙으면 오른쪽 값들 중 할당되고 남은 값들이 * 연산자가 붙은 변수에 할당된다.

x, *y = 1,2,3,4 #즉 1개 빼고 나머지 다 라는 말이 된다.
print(x)
print(y)
*x,y = 1,2,3,4
print(x)
print(y)

#네임드 튜플 -> 파이썬 표준 모듈 collections에는 네임드 튜플이라는 시퀀스 데이터 타입이 있다. 네임드 튜플은 일반 튜플과 비슷한 성능과 특성을 갖지만 튜플 항목을 인덱스 위치 뿐만 아니라 이름으로도 검색 가능함

import collections
person = collections.namedtuple('person','name age gender')
p = person('hyunskki',30,'M')
print(p)
print(p.name)
#음 잘 이해가 되지 않는다. 나중에 쓸일이 있으면 다시 한번 보자

#list 일반적으로 CS에서 배열은 여러 요소(원소)들이 연속된 메모리에 순차적으로 저장되는 간단한 구조이다. 연결리스트(linked list)는 여러 분리된 노드가 서로 연결되어있는 구조이다.
#순회시 링크드리스트의 시간복잡도는 직접 접근하는것보다 오래걸린다(처음부터 순회해야하기 때문에) 하지만 insert를 할 때 시간복잡도는 위치만 알고 있다면 배열보다 낮다. 배열은 모든 항목을 옮겨야하기 때문이다.
#파이썬에서 배열과 유사한 객체는 리스트이다. 리스트는 크기를 동적으로 조정할 수 있는 배열이고 링크드리스트와 연관이 없다. 또한 리스트는 가변타입이기 때문에 복사 시 잘 해야한다.
#리스트 끝에서 항목을 제거하거나 추가할때 append나 pop을 사용하고 시간복잡도는 o1이다. 리스트 항목을 검색해야하는 remove index, insert in등의 복잡도는 O(n)이다. 
#빠른 검색이 필요하면 set이나 dict를 사용하는 것이 적합하다. 

#리스트에는 append메서드가 있다. 끝에 추가하는것이고 잘 알고있기 때문에 넘어간다.
#또 다른 메서드로 extend()가 있다. A.extend(c)로 되어있고, c를 리스트 A에 추가한다. 
list1 = ['aa','bb']
list1.extend('cc') #이렇게 하면 반복가능한 c c가 나뉘어져서 추가가된다.
print(list1)
list1.extend(['cc']) #이렇게하면 정상적으로 list끼리 합쳐지는 것을 볼 수 있다.
print(list1)
list1 = ['aa','bb']
list2 = ['cc','dd']
list1.extend(list2)
print(list1)
#이런식으로 두 리스트를 합칠 수 있다.

#insert() A.insert(index,value) 이고 인덱스 위치에 value를 끼워넣는다.
list1 = ['aa','bb']
list1.insert(1,'cc')
print(list1)
#A.remove(x)는 A리스트 안에 x값을 제거한다. 
list1.remove('cc')
print(list1)
#A.pop(x)은 리스트 A에서 x인덱스에 있는 값을 제거하고 그 값을 반환한다. 만약 인덱스를 지정해주지 않으면 맨 끝에 있는 값을 빼고 반환해준다.
a = list1.pop(0)
print(a)
print(list1)
#del문은 리스트 인덱스를 지정하여 특정한 항목을 삭재한다. 그뿐만 아니라 슬라이스를 사용하여 특정범위 항목들을 제거할 수 있다.
a = [-1,4,5,7,10]
del a[0]
print(a)
del a[:2]
print(a)

#index문은 리스트에서 해당 원소(value)의 위치를 반환해준다.
print(a.index(7))

#count 메서드는 해당 원소가 몇개 들어가있는지 세어준다.
list1 = [1,2,3,1,1,2,4]
print(list1.count(1)) #1은 3개가 들어있으니 3이 출력됨

#sort()메서드는 리스트를 정렬하여서 적용해준다. A.sort(key, reverse) 아무 조건이 없으면 오름차순으로 정렬해준다.
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#reverse()는 리스트 A의 항목들을 반전시켜서 적용시켜준다. list[::-1]과 같다
list1 = [1,2,3,4]
list1.reverse()
print(list1)
list1 = list1[::-1]
print(list1)

#언패킹은 비슷하게 사용한다.
first, *rest = list1
print(first)
print(rest)
#또한 함수에 전달시 다음과 같이 전달할 수 있다.
def multiple(a,b,c):
    return a*b*c

result = multiple(*rest)
print(result)

#리스트 컴프리헨션(list comprehension)은 반복문의 표현식이다. 조건문도 포함할 수 있고, 다음과 같이 표기한다.
#[항목 for 항목 in 반복가능한 객체]
#[표현식 for 항목 in 반복가능한 객체]
#[표현식 for 항목 in 반복가능한 객체 if 조건문]
#이렇게 표현할 수 있는데 이대로는 살짝 어려워보일 수 있으니, 예제를 통해서 알아보자
a = [y for y in range(10) if y%4 == 0] #0 4 8
print(a)
b = [2**i for i in range(10)] #2의 제곱들
print(b)
#리스트 컴프리핸션은 단순한 경우에만 사용하는 것이 좋다.
#속도의 경우 concat이 가장 느리고, append가 그 다음이며 컴프리핸션이 두번째로 빠르고, range가 가장 빠르다.

#바이트와 바이트배열 (byte, bytearray)는 원시 바이트(raw)를 처리하는데 사용할 수 있는 데이터타입이다. 바이트 타입은 문자열타입과 비슷하고, 불변형이다. 바이트배열은 리스트타입과 비슷하고 가변형이다.

#비트와 비트연산자 -> 비트연산자는 비트로 표현된 숫자를 조작하는데 유용하다. 예를들어서 곱셈연산자 대신에 비트연산자로 곱셈을 할 수 있다.
#1<<x는 1을 x번 왼쪽으로 이동 즉 2^x 를 빠르게 구할 수 있다. 또한 x&(x-1)이 0인지 확인하면 x가 2의 제곱인지 빠르게 확인할 수 있다.
x = 4

print(1<<x) #2^4
x = 8
print(x&(x-1)) #2의 제곱에 포함되어있으므로 0이 나옴
x = 6
print(x&(x-1)) #2의 제곱값이 아니므로 다른 값이 나옴

#연습문제 안녕 세상! 을 !상세 녕안 으로 바꿔보자
a = '안녕 세상!'
b = a[::-1]
print(b)

#문자열 단위 단어로 반전하기 
a = '파이썬 알고리즘 정말 재미있다'
b = a.split(' ')
#print(b)
b.reverse()
print(b)
c = ''
for i in b:
    c += i+' '
print(' '.join(b))

print(c)

#단순 문자열 압축 은근 자주보였던 내용이다, counter를 사용할 수도 있겠지만 직접 짜보자
a = 'aabccccaaa'
def comp(s):
    count, last = 1, ""
    list1 = []
    for i,c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i !=0:
                list1.append(str(count))
            list1.append(c)
            count = 1
            last = c
    list1.append(str(count))
    return ''.join(list1)

print(comp(a))

#문자열 순열 (permutation)은 몇개중 일부를 골라서 순서를 고려해 나열한 경우의수임
import itertools

def perm(s):
    res = itertools.permutations(s)
    return [''.join(i) for i in res]

a = '012'
print(perm(a))


def comb(s):
    res = itertools.combinations(s,2)
    return [''.join(i) for i in res]

print(comb(a))

#이렇게해서 어떻게 시퀀스 형식을 다루는지 알게 되었고, 새로운 것도 알게 되었다. 하지만 이 책에서 빠진 내용같은게 존재한다. 어떤게 속도가 빠르고 그런지 알게되었고, 깊은 복사의 개념또한 알게되었다.
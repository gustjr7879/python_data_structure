#컬렉션(collection)자료구조는 시퀀스 자료구조와 달리 데이터를 서로 연관시키지 않고 모아두는 컨테이너이다. 셋과 딕셔너리가 있다.
#연관시키지 않아서 검색과 같은 작업에서 빠르게 수행할 수 있다. 
#파이썬의 set은 집합이고, 반복가능하고 가변적이고 중복요소가 없다. 중복요소가 없기 때문에 합집합, 교집합 차집합등을 쉽게 구할 수 있다.
#셋의 삽입 시간복잡도는 1이고 합집합은 o(m+n)이다. 교집합은 둘 중 작은것만 계산하면 되므로 o(n)이다.
#프로즌 셋이라고 존재하는데 이는 가변성을 불변성으로 바꿔준다.

#set의 메서드에 대해서 알아보자
#A.add()는 셋에 x가 없을 경우 x를 추가해주는 것이다.
name = {'a','b','c'}
name.add('d')
print(name)
#A.update(b)와 A|=b 연산자는 A에 b를 추가해준다. (합집합 연산자)
name.update({'e','g'})
name|={'f'} 
print(name)
#union 연산자는 update와 |= 연산자와 같지만 연산결과를 복사본으로 반환한다. (깊은 복사)
#intersection() 과 & 연산자는 교집합의 복사본을 반환해준다.
a = {'a','b'}
b = {'b','c'}
print(a&b)
print(a.intersection(b))
#difference()와 -연산자는 차집합의 복사본을 반환해준다.
print(a.difference(b))
print(a-b)
#clear()는 모든 항목을 제거해준다.
print(a.clear())
#discard()는 value를 제거하고 반환값은 없다. remove는 discard()와 같지만 반환할게 없으면 error를 발생시킨다. pop()은 무작위로 제거하고 그 값을 반환해준다.
print(b.pop())
#set과 리스트는 서로 변환해줄 수 있고 딕셔너리에서도 셋 속성을 이용할 수 있다. 
#파이썬 딕셔너리는 해시테이블로 구현되어있다. 해시함수는 특정 객체에 해당하는 임의의 정수 값을 상수 시간 내에서 계산해준다. 이 정수는 연관 배열의 인덱스로 사용된다.
print(hash(42))
print(hash('hello'))
#해시 테이블은 키와 값이 연관되어있고, 키를통해 연관된 값을 얻는 연관배열을 구현하는데 사용된다.
#컬렉션 매핑타입인 딕셔너리는 반복가능하다. in연산자와 len()함수 또한 지원한다. 매핑은 key-value로 되어있고 각 항목에 대한 메서드를 제공한다.
#모든 항목은 고유하기 때문에 각 항목에 접근하는 시간복잡도는 1이다. 하지만 항목의 삽입순서를 기억하지 않고 그러기 때문에 슬라이스를 사용할 수 없다.

trantino = {}
trantino['name'] = '타란티노'
trantino['job'] = '감독'
print(trantino)

sogae = dict({'name':'hyunskki','age':26,'degree':4})
print(sogae)
#딕셔너리의 메서드에 대해서 알아보자.
#setdefault() 메서드는 딕셔너리에서 키의 존재 여부를 모른채 접근할 때 사용된다. 원래 딕셔너리에 존재하지 않는 키에 접근하면 예외가 발생한다. A.setdefault(key,default)를 사용하면 A에 key가 있다면 value를 얻을 수 있고 key가 존재하지 않는다면 새 키와 기본 값 default가 딕셔너리에 저장된다.
dicta = {}
dicta.setdefault('name','hyunskki')
print(dicta)
a = dicta.setdefault('name','sss') #name key가 존재하기 때문에 value를 받음
print(a)
#A.update(B)는 딕셔너리 A에 딕셔너리 B의 키가 존재한다면 기존 A의 key value를 B의 key value로 갱신해준다. 존재하지 않는다면 추가한다.
b = dict({'name':'kkk'})
dicta.update(b)
print(dicta) # name키가 존재하기 때문에 kkk로 바뀜
c = dict({'age':22})
dicta.update(c)
print(dicta) #없기 때문에 추가되는 것을 확인할 수 있음
#A.get(key)는 딕셔너리 A의 key가 가지고 있는 value를 반환한다. key값이 없다면 아무것도 반환하지 않는다.
print(dicta.get('name'))

#items(),keys(),values()는 딕셔너리 뷰이다. items는 전체 다 보여주고, keys는 key값만, values는 values값만 보여준다.
#pop(),popitem()는 key항복을 제거한 후 그 value를 반환하거나, popitem은 맨뒤항목의 key와 value를 반환해준다.
print(dicta.pop('name')) #name의 value만 반환
print(dicta)
print(dicta.popitem()) #맨 마지막 항목의 key와 value반환
#clear()는 제거한다.
#딕셔너리는 조회, 할당, 삭제,in,반복에서 1의 시간복잡도만 가지고 있다.

#딕셔너리 순회 : 반복문에서 딕셔너리를 순회할때는 기본적으로 key만 사용한다. 원래는 임의의 순서대로 정렬되어있지만. sorted()함수를 사용하면 정렬된 상태로 순회가 가능하다.
#sorted함수는 딕셔너리의 keys, values, items에 대해서 사용할 수 있다.
d = dict({'c':'!','b':'world','a':'hello'})
print(sorted(d.values())) #이런식으로 keys로 정렬할 것인지 values()로 정렬할 것인지 설정 가능하다.
for i in sorted(d):
    print(i,d[i])

#딕셔너리 분기 원래 분기를 할때 주로 if를 사용하여 분기를 하는데, 딕셔너리로도 분기를 할 수 있다. 하지만 주로 사용되지 않을것 같으니 if를 사용하도록 하자

#파이썬 컬렉션 데이터 타입 파이썬의 collections 모듈은 다양한 딕셔너리 타입을 제공한다.
#기본 딕셔너리는 collections.defaultdict 모듈에서 제공하는 추가 딕셔너리 타입이다. Orderdict는 삽입순서대로 항복을 저장한다.
#counter 딕셔너리는 객체를 카운팅해주는 서브클래스이다. collections.Counter로 사용한다.
from collections import Counter

seq1 = [1,2,3,5,1,2,5,5,2,5,1,4]
seq_counts = Counter(seq1)
print(seq_counts)
#항목의 발생횟수를 수동으로 갱신하거나 update를 사용할 수 있다.
seq2 = [1,2,3]
seq_counts.update(seq2) # seq2가 추가되어서 (update는 합집합 연산자임) 계산이 된다.

print(seq_counts)

#연습문제 : 단어 횟수세기
#collections.Counter의 most_common()을 사용하면 문자열에서 가장 많이 나오는 단어와 횟수를 가져올 수 있다.
seq = '버피 에인절 몬스터 잰더 윌로 버피 몬스터 슈퍼 버피 에인절'
n_seq = seq.split(' ')
print(n_seq)
cnt_seq = Counter(n_seq)
print(cnt_seq)
print(cnt_seq.most_common(3))

#애너그램은 문장 또는 단어의 철자 순서를 바꾸는 놀이를 말한다. 두 문자열이 서로 애너그램인지 확인하고 싶다고 하면, 이때 딕셔너리가 가장 유용하게 사용된다.
#발생횟수의 차이가 0이면 애너그램이기 때문이다.
#다른 방법으로는 해시함수의 속성을 이용할 수 있는데 ord()함수는 인수가 유니코드 객체일때 유니코드를 나타내는 정수를 반환한다. 이 모든 문자의 ord()함수 결과가 같으면 두 문자열은 애너그램이다.
s1 = 'google'
s2 = 'ggoole'

s1_sum = 0
s2_sum = 0
for i in range(len(s1)):
    s1_sum += ord(s1[i])
    s2_sum += ord(s2[i])

if s1_sum == s2_sum:
    print('애너그램')


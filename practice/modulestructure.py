#2023 8 23 모듈과 구조
#파이썬에서 모듈은 def를 사용해서 정의된다. return값을 지정해주지않으면 None을 반환하게된다.
#모듈을 사용할 때 함수 또는 메서드에서 가변객체를 기본값으로 사용하면 안된다. 예를들면
def append(number, number_list=[]):
    number_list.append(number)
    return number_list
#는 나쁜 예시이고
def append(number, number_list=None):
    if number_list == None:
        number_list = []

    number_list.append(number)
    return number_list
#는 좋은 예시이다.

# __init__.py 파일에 대해서
#패키지는 모듈과 __init__.py파일이 있는 디렉터리이다. 파이썬은 이 파일이 있어야지 패키지로 취급한다.
#모듈을 검색할 때 string과 같이 흔한 이름의 디렉터리에 있는 경우 검색되지 않는 상황을 방지하기 위함이다.
#패키지는 import 폴더이름.파일모듈명 으로 불러올 수 있다.
#파이썬은 모듈을 임포트 할때마다 __name__이라는 변수를 만들고 모듈 이름을 저장한다. 이 내용은 hello.py에서 진행한다. __main__때문이다.
#파이썬 실행 시 -0 를 붙여서 실행하면 최적화된 코드가 생성되어서 .pyc에 저장된다.

#sys 모듈에 대해서 
#sys.path는 인터프리터가 모듈을 검색할 경로를 담은 문자열 리스트이다. sys.path 변수는 PYTHONPATH 환경변수로 초기화된다.
#환경 변수를 수정하면 모듈 경로를 추가하거나 임시로 모듈 경로를 추가할 수 있다.
import sys
print(sys.path)
#sys.argv 변수를 사용하면 프롬프트에서 전달된 인수를 프로그램 내에서 사용할 수 있다.
def test():
    for arg in sys.argv[1:]:
        print(arg)
test()
#dir() 내장함수는 모듈이 정의하는 모든 유형의 이름(모듈 변수 함수)를 찾는데 사용된다.
print(dir(sys)) #이처럼 sys에 있는 모든 모듈을 뽑아서 확인할 수 있다. 

#False True정의 False는 0 None 그리고 빈 시퀀스들이 False로 구분되고 나머지는 True로 구분된다.

# 파이썬에서 제너레이터는 이터레이터를 작성하는 편리한 방법이다. 객체에 __iter__()와 __next__() 메서드를 둘 다 정의하면 이터레이터 프로토콜을 구현한것이다.
#이때 yield 키워드를 사용하면 편리하다.
#호출자가 메서드를 호출할 때 return 키워드는 반환값을 반환하고 메서드를 종료한 후 호출자에게 제어를 반환한다. 반면 yield 미워드는 각 반환값을 호출자에게 반환하고 반환값이 모두 소진되었을 때
#메서드가 종료된다.
# 즉 return은 코드 종료 후 값을 반환해주는 반면, yield는 호출될때마다 값을 반환해준다.
a = [1,2,3]
def f(a):
    while a:
        yield a.pop()

print(next(f(a)))
print(next(f(a)))
print(next(f(a)))
#yield는 나중에 다시 공부해보도록 하자

#break 대 continue 반복문에서 break키워드를 만나면 바로 반복문을 빠져나간다. 반복문에서 continue를 만나면 반복문의 다음 단계로 넘어간다.
#반복문에서는 else절을 사용할 수 있는데 이는 반복문이 종료되었을 때(for문을 모두 순회했거나 while문에서 조건이 False가 될 때) 실행된다.
for i in range(10):
    if i % 2 == 0:
        continue #바로 다음 조건으로 넘김
    print(i)
else:
    print('end')

#range는 숫자 리스트를 만들어준다. enumerate()는 반복가능한 객체의 인덱스값과 항목값의 튜플을 반환해준다.
a = [i for i in range(10)]

for i, v in enumerate(a):
    print('{}번째 값 {}'.format(i,v))
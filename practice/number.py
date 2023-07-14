#파이썬에서 숫자는 정수, 부동소수점, 복소수로 나타내진다
#파이썬에서 정수는 int로 나타내고 불변(immutable)형이다. 파이썬 정수의 크기는 컴퓨터 메모리에 의해 제한된다.
#정수를 표현하는데 필요한 바이트 수를 확인하려면 (int).bit_length()를 사용

a = 32
print(a.bit_length()) # 6

#어떤 문자열을 정수로 변환(casting)하거나 다른 진법의 문자열을 만들려면 int(문자열,밑)을 사용하자
b = '11'
print(int(b)) # 11
print(int(b,2)) # 3 이 경우 밑 범위의 숫자를 벗어나는 값을 입력하면 value error가 뜸

#부동소수점 -> 파이썬에서 부동소수점은 float로 나타내고 불변형이다. 교수님한테 배웠던것처럼 1비트는 부호를 나타내고 23비트는 유효숫자자리수(가수) 8비트는 지수이다.
#부동소수점은 이진수 분수(binary fraction)으로 표현되기 때문에 함부로 비교하거나 빼면 안된다.
#이진법으로 표기할때 순환된다면 차이가 나게되기 떄문이다.동등성 테스트는 사전에 정의된 정밀도 범위 내에서 수행되어야한다.
#unittest 모듈에 assertAlmostEqual()메서드 같은 접근법을 사용한다.
#또한 부동소수점의 숫자는 메모리에서 비트패턴으로 비교할 수 있다. 먼저 부호 비교를 별도로 처리하고, 두 숫자가 음수이면 부호를 뒤집고 숫자를 반전하여 비교한다. 지수패턴이 같으면 가수를 비교한다.
#파이썬에서 나누기연산자는 항상 부동소수점을 반환한다. (/) , 하지만 (//)연산자를 이용하면 정수를 반환시킬 수 있다. (%)를 사용하면 나머지를 구하고, divmod(x,y)를 이용하면 x를 y로 나눈 몫과 나머지를 얻는다
print(divmod(5,4)) # 1,1 
#round(x,n)의 경우 n이 음수인 경우 x를 n만큼 반올림한 값을 반환하고 양수인경우 x를 소수점 이하 n자리로 반올림한 값을 반환한다.
print(round(100.96,-2)) # 100 
print(round(100.96,2)) # 100.96 소수점 이하 2자리

#복소수는 z= 3+4j와 같이 생긴 부동소수점 한쌍을 갖는 불변형이다.
#z.real z.imag, z.conjugate() 같은 메서드로 실수부, 허수부, 켤레 복소수를 구할 수 있다. 복소수를 사용하려면 cmath모듈을 임포트해야하는데 이 모듈은 math에 있는 삼각함수와 로그함수의 복소수 버전을 제공함

#fraction모듈 . 파이썬에서 분수를 다루려면 fraction모듈을 사용한다. 

from fractions import Fraction

def rounding_floats(num1,place):
    return round(num1,place) 

def float_to_fractions(number):
    return Fraction(*number.as_integer_ratio())

def get_denominator(num1,num2):
    #분모를 반환한다.
    a = Fraction(num1,num2)
    return a.denominator

def get_numerator(num1,num2):
    #분자를 반환한다.
    a = Fraction(num1,num2)
    return a.numerator

def test_testing_floats():
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num6 = 6
    assert(rounding_floats(num1,num2)==1.2)
    assert(rounding_floats(num1*10,num3)==10)
    assert(float_to_fractions(num1)==num4)
    assert(get_denominator(num2,num6)==num6)
    assert(get_numerator(num2,num6)==num2)
    print('테스트 통과 !')

test_testing_floats()

#decimal모듈을 통하여 부동소수점을 빠르게 비교할 수 있다.
#실습은 필요할때 검색해보자

#2진수, 8진수 16진수
#bin(i)를 통하여 i의 2진수 문자열을 반환할 수 있다. oct(i)는 8진수 hex(i)는 16진수를 반환해줌

#최대공약수 
def find_GCD(num1,num2):
    while(num2 !=0):
        result = num2
        num1,num2 = num2, num1%num2
    return result    
#간단하지만 복잡하게 표현되던 코드를 간략하게 만들어주는 재귀를 활용한 수식
print(find_GCD(21,12)) # 3

#random 모듈 -> 난수를 생성하는 random모듈, 난수이기 때문에 출력결과는 계속 변함 단, seed를 고정해주면 고정됨

import random

def testing_random():
    #random 모듈 테스트
    values = [1,2,3,4,5]
    print(random.choice(values))
    print(random.sample(values,2))

    random.shuffle(values)
    print(values)

    print(random.randint(0,10)) # 0에서 10사이 랜덤값
    print(random.random()) # 0에서 1사이에 랜덤값

print(testing_random())

#피보나치 수열(fibonacci sequence) 알고리즘하면 생각나는... 재귀로 풀어야하는..
#만약 숫자 4가 주어지면 4번째 피보나치 수열을 구하는 알고리즘을 만들어보자

def fib(n):
    a = 1
    b = 1
    cnt = 3
    while cnt <=n:
        c = a+b
        a = b
        b = c
        #print(a,b)
        cnt +=1
    return c

print(fib(6))    
#내가 짠 코드는 제네레이터를 사용한 코드와 유사하다. yield를 사용하므로 나중에 공부하고 다시하도록 한다.

#소수를 구하는 방법(prime number)
#브루트포스를 사용한 코드와 제곱근을 활용한 코드가 있다. 
def find_prime(num):
    num = abs(num)
    if num < 4:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
print(find_prime(6))

#numpy 패키지는 파이썬 프로그래밍 언어의 확장 패키지이고 대규모 배열 및 행렬을 지원한다. 또한 배열이나 행렬 연산에 사용되는 수학 함수 라이브러리를 사용한다.
#넘파이 배열은 임의의 차원을 가진다. np.array이고, 시퀀스의 시퀀스를 2차원 넘파이 배열로 생성가능하다.
import numpy as np

x = np.array(((11,12,13),(21,22,23)))
print(x)
print(x.ndim) # x.ndim 은 차원을 알려준다. 이외에도 여러가지 연산기능과 찾기기능이 있다.

#### chapter 1종료 : 내가 아는부분은 어느정도 넘어가서 빨리끝낼 수 있었다. 하지만 몰랐던 부분도 존재하고 이번기회로 한번 훑었고 나중에 나올때마다 상기해서 기억을 하도록 하자


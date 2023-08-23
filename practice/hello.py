hello = 'hello'
def world():
    return "world"

if __name__ == "__main__":
    print("{} 직접 실행됨".format(__name__))
else:
    print("{} 임포트됨".format(__name__))
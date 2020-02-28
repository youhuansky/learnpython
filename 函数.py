def printmy(a1):
    print(a1)


printmy("这是我的第二个函数")


def summy(a, b, c):
    print(a + b + c)


summy(1, 2, 3)


def test1(a):
#    a[0] = 30
    a = 30
    print(a)

a = 10
#a = [10, 20, 30]
test1(a)
print(a)


def test2(*a):
    result = 0
    for num in a :
        result += num
    print(result)


test2(123, 456)
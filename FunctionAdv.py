#位置参数

def pow(x):
    return x * x
print(pow(3))
#可定义多个参数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(pow(2,3))

#默认参数
def powerdefault(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(powerdefault(3))
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数最大的好处是能降低调用函数的难度。
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
#只有与默认参数不符的学生才需要提供额外的信息：
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

#定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
#如果L是一个list那么会每次增加一个END

#可变参数

#计算a2 + b2 + c2 + ……。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#调用的时候，需要先组装出一个list或tuple
cal=[1,3,5]
print(calc(cal))

#利用可变参数，调用函数的方式可以简化
def calcu(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

#如果已经有一个list或者tuple，要调用一个可变参数
print(calcu(cal[0], cal[1], cal[2]))
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums=[1,2,3,4]
print(calcu(*nums))

#关键字参数
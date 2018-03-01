#生成器

#创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(next(g))
print(next(g))
#每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
g = (x * x for x in range(10))
#调用
for n in g:
    print(n)

# 斐波那契数列
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'
#赋值语句等价于
#t = (b, a + b) # t是一个tuple
#a = t[0]
#b = t[1]

#把函数改成generator只需要把print(b)改为yield b
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f = fib(6)

#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step1')
    yield 1
    print('step2')
    yield (3)
    print('step3')
    yield (5)
o = odd()
print(next(o))
print(next(o))
print(next(o))


#用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print(g)

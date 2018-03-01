#Python内建的filter()函数用于过滤序列。


#判断是否奇数
def is_odd(n):
    return n%2==1

#过滤
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

#删除序列中的空字符串

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
#filter()函数返回的是一个Iterator，也就是一个惰性序列，
#所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#用filter求素数
#先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0

#定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。
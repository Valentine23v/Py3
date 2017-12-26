#Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
#由于字符串也是可迭代对象，因此，也可以作用于for循环：

for ch in 'ABC':
    print(ch)
#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#判断一个对象是可迭代对象通过collections模块的Iterable类型判断：

from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
print(isinstance([1,2,3], Iterable)) # list是否可迭代
print(isinstance(123, Iterable)) # 整数是否可迭代

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print("---------------")
#同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

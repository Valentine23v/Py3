#用r'' 处理转义字符
print(r'\\\t\\')

#用ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord("A"))
print(chr(25991))

#Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('中文'.encode('utf-8'))
#读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#要计算str包含多少个字符，可以用len()函数
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
#1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
#在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

#格式化
#%为占位符%d	整数%f	浮点数%s	字符串%x	十六进制整数
print('Hi, %s, you have $%d.'% ('Michael', 1000000))
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d %%' % 7)
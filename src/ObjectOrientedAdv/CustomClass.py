# 定制类

# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('Michael'))
#<__main__.Student object at 0x109afb190>

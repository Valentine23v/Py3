# 获取对象信息

#使用type()
#判断对象类型，使用type()函数：
#基本类型都可以用type()判断：
print(type(123))
print(type('str'))
print(type(None))


#如果一个变量指向函数或者类，也可以用type()判断：
class Dog(object):
    def eat(self):
        print('eeee')

print(type(abs))
d=Dog()
print(type(d))

#type()返回的是class类型如果需要判断就要比较两个变量的type是否相同
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)

#使用isinstance()
#可以用and
print(isinstance(d,Dog) and isinstance(d,list))
#判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir('ABC'))


#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

print(len('ABC'))
print('ABC'.__len__())

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x

obj = MyObject()

print(hasattr(obj,'x'))#有属性x吗？
print(obj.x)

print(hasattr(obj,'y'))#有属性y吗？

setattr(obj,'y',19)#设置一个属性'y'
print(hasattr(obj,'y'))#有属性y吗？

print(getattr(obj,'y'))#获取属性y

#如果试图获取不存在的属性，会抛出AttributeError的错误：
getattr(obj, 'z') # 获取属性'z'
#可以传入一个default参数，如果属性不存在，就返回默认值：
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
#也可以获得对象的方法：
print(hasattr(obj, 'power')) # 有属性'power'吗？
print(getattr(obj, 'power')) # 获取属性'power'

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn) # fn指向obj.power
print(fn()) # 调用fn()与调用obj.power()是一样的


# 总结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
# sum = obj.x + obj.y
# 就不要写：
# sum = getattr(obj, 'x') + getattr(obj, 'y')

# 一个示例

#def readImage(fp):
#    if hasattr(fp, 'read'):
#        return readData(fp)
#    return None

# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

#请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

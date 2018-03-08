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

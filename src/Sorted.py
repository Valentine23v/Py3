#Sorted


#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
#结果[-21, -12, 5, 9, 36]

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))
#结果[5, 9, -12, -21, 36]

#对字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#结果['Credit', 'Zoo', 'about', 'bob']

#不区分大小写的话
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#结果['about', 'bob', 'Credit', 'Zoo']

#进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def byname(t):
    return t[0]

def byscore(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#按名字排序
print(sorted(L,key=byname))
#按成绩排序
print(sorted(L,key=byscore,reverse=True))
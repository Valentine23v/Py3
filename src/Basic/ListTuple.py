#List 用[]
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
#len()取长度
print(len(classmates))
#负索引从后往前查找元素
print(classmates[-2])
#在末尾插入元素 append
classmates.append('Adam')
#在某个位置插入元素 insert
classmates.insert(1,'Jack')
#删除末尾元素
classmates.pop()
#删除指定位置元素
classmates.pop(2)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[2]='Two'
#list里面的元素的数据类型也可以不同,list元素也可以是另一个list
L=['Apple', 123, True]
s=['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])

#Tuple
#元素不可变，更安全 用()
classmates = ('Michael', 'Bob', 'Tracy')
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
#"可变"的Tuple 其实是指向不能变，其中的list元素可以被修改
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'

print(t)
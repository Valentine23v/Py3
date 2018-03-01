#Dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Bob"])

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 87
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)


#Set
s = ([1,2,3])
print(s)
#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
#通过remove(key)方法可以删除元素
s.remove(4)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

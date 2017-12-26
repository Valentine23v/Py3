#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3元素
r=[]
n=3
for i in range(n):
    r.append(L[i])

print(r)

#使用L[：3]即可切片
print(L[:3])
print(L[1:3])#也可从索引1开始取
print(L[-2:])#倒数切片
print(L[-2:-1])#倒数第一个元素是-1

L= list(range(100))
print(L[:10:2])#前10个数每两个取一个
print(L[::5])#所有数每5个取一个

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])
#字符串'xxx'也可以看成是一种list
print('ABCDEFG'[:3])
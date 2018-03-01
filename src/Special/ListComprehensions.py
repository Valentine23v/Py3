#列表生成式

print(list(range(1,11)))#生成1-10

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
#可用列表生成式代替
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环
print([x * x for x in range(1, 11)])
#for循环后面还可以加上if判断
print([x * x for x in range(1,11) if x%2==0])
#使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

#列出当前目录下的所有文件和目录名
import os
print([d for  d in os.listdir('.')])
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])
#把一个List中的所有字符串变成小写
L=['Hello','World','IBM','Apple']
print([word.lower() for word in L])
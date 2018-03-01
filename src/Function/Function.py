#调用函数
print(abs(20))
print(abs(-30))
print(max(2, 3, 1, -5))

#定义函数
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return

#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）

#空函数
def nop():
    pass
#pass还可以用在其他语句里，比如：
age=20
if age >= 18:
    pass

#类型检查
#数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    if x<0:
        return -x


#返回多个值
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#其实这只是一种假象，Python函数返回的仍然是单一值 返回了一个Tuple
r = move(100, 100, 60, math.pi / 6)
print(r)


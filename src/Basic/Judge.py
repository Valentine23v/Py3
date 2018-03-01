#条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
#elif
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#if判断条件还可以简写
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x='A'
if x:
    print('True')

#input需要注意
s = input('birth: ')
birth = int(s)#input输入类型是str 需要转类型
if birth < 2000:
    print('00前')
else:
    print('00后')
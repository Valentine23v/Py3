# 实例属性和类属性

class Student(object):
    name = 'Student'

s = Student()
print(s.name)# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)# 打印类的name属性

s.name='Micheal'
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

#总结
#实例属性属于各个实例所有，互不干扰；
#类属性属于类所有，所有实例共享一个属性；
#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
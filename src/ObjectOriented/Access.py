#访问限制

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改

class Student(object):

    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


#使用get set 方法来获取修改内部属性
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
#set的时候可以通过参数检查避免无效参数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
#有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 错误写法：
# >>> bart = Student('Bart Simpson', 59)
# >>> bart.get_name()
# 'Bart Simpson'
# >>> bart.__name = 'New Name' # 设置__name变量！
# >>> bart.__name
# 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
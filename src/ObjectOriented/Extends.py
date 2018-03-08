# 继承和多态

class Animal (object):

    def run(self):
        print('Animal is running...')

#python的继承写括号里
class Dog (Animal):

    def eat(self):
        print('eat meat')
class Cat (Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('eat fish')

dog=Dog()
cat=Cat()

dog.eat()
cat.run()

# 判断一个变量是否是某个类型可以用isinstance()判断

isinstance(dog,Dog)
isinstance(dog,Animal)

# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：

def run_twice(animal):
    print('***')
    animal.run()
    animal.run()

run_twice(cat)

# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
#对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。


#总结
#继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
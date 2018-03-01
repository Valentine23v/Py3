#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块

' a test module '
#任何模块代码的第一个字符串都被视为模块的文档注释；

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


#从别的文件调用时
#import hello
#hello.test()
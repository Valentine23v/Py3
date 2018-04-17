# 枚举类

from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数。


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday(3))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量

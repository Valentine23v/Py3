#Python内建的filter()函数用于过滤序列。


#判断是否奇数
def is_odd(n):
    return n%2==1

#过滤
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

#删除序列中的空字符串

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
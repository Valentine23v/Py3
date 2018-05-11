# 文件读写

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法

with open('/path/to/file', 'r') as f:
    print(f.read())


# 使用三重引号来格式化字符串
a = '''锄禾日当午，
   汗滴禾下土'''
print(a)

# int太长用下划线来分隔，便于阅读代码
b = 123_456
print(b + 1)

# 字符串引号前使用f标识，引号中使用 {变量}，来变量拼接
c = f'haha {a}'
print(c)

# 布尔值其实也是整型 True是1，False是0
d = True
print(d + 1)
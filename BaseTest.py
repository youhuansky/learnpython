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

#python判断数据类型：type()用来检查值的类型
print(type(None))

print(id(d))

#int()可以将其他的对象转换为整型，不会对原来的变量产生影响
# a = int(a)
# print(a)
# print(type(a))
print (3 and 2)
#三元运算符
print('你好') if True else print('hello')
# list是python中的一个对象
# 1.创建列表
# 创建了一个空列表
my_list = []
print(type(my_list))
my_list = [10, 40, 50]

# 通过index获取列表中的元素
print(my_list[0])

# 通过len函数获取长度
print(len(my_list))

print(my_list[:])

print(10 in my_list)

my_list[0] = 90
# 通过del删除执行下标的内容
# del my_list[0]
# 通过切片进行赋值，只能使用序列赋值

my_list[0:2] = [99, 88]

print(my_list)

# 使用my_list[0:0] 再指定位置插入数据
my_list[0:0] = [199, 188]
print(my_list)

stud = ["123", "345", "8790"]
print(stud)
# 使用append向尾部插入一个元素
stud.append("567")
print(stud)

# 使用insert向指定位置插入元素
stud.insert(2, "zxcv")
print(stud)

# extend 使用新的序列拓展,相当于 list += list
stud.extend(["zxcvsf", "32434"])
print(stud)

stud.sort(reverse=True)
print(stud)

###遍历列表
#for循环的代码块会执行多次，序列中有几个元素就执行几次

for indexobj in stud:
    print(indexobj)

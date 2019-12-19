# 元祖tuple
# 元组是一个不可变的序列
my_tuple = ()
print(id(my_tuple))
my_tuple = (1, 2, 3, 4, 5)
print(id(my_tuple))

#解包时，变量的数量和元组中的数量必须一样，可以用*表示省略，那么c就变成了剩余变量的数组
a,b,*c = my_tuple

print(a)
print(my_tuple[1])
a,b,c,d,e = my_tuple
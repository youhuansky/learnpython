# 使用{}创建字典
d = {}
d = {"name": "youhuan"}
print(d)

# dict创建一个序列
a = dict(name="youhuan")
print(a)
# len获取字典键值对的个数

# in，not in 检查字典中是否包含指定的键

# 获取字典中的值
print(d.get("name2", "moren"))
print(d["name"])

#修改字典中的值
d["name"] = "miaomiao"
print(d)
#setdefault()向字典中添加值，如果不存在则添加，如果存在就不做任何操作

#update()用于合并两个字典，如果有重复的key，新的会替换旧的

#popitem()弹出最后一个键值对，返回的是一个元组

#pop()根据key弹出字典中的值

#遍历字典
keys = d.keys()
for i in keys:
    print(d.get(i))

items = d.items()

for k, v in items:
    print(k, "  =>  ", v)
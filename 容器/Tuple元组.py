"""
声明语法:
tuplename=(元素,元素,元素);
特点：
1.有序、不可变、允许重复元素、可存储任意类型数据
2.使用圆括号 () 定义（单个元素需加逗号）
3.创建后无法修改，删除，增加元素
"""
"""
列表和元组在 “读取（遍历等） / 查询” 类操作上几乎一致，列表可变，元组不可变
"""
tuple_01 = (1,2,3,4)
print(tuple_01)


tuple_002 = ()
print(type(tuple_002))
tuple_0002 = (15)#使用圆括号 () 定义（单个元素需加逗号）
print(type(tuple_0002))
tuple_02 = (5,)#声明一个元素的元组
print(tuple_02)
print(type(tuple_02))

#查找指定元素首次出现的索引
a = tuple_01.index(4)
print(a)

#统计指定元素出现的次数
b = tuple_01.count(4)
print(b)

#最大值最小值
c = max(tuple_01)
print(c)
d = min(tuple_01)
print(d)

#获取长度
e = len(tuple_01)
print(e)

#遍历
for i in tuple_01:
    print(i)

for i in range(0,len(tuple_01),1):
    print(i)

z = 0
while z < len(tuple_01):
    print(tuple_01[z])
    z += 1

#元组和列表是可以相互转换的,列表转换为元组使用tuple(),元组转换为列表使用list();
list_01 = list(tuple_01)
print(list_01)

tuple_01 = tuple(list_01)
print(tuple_01)

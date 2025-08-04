#for in循环遍历列表
list_01=["jack","rose","tom","lucy","jeery","jack","张三"]
for name in list_01:
    print(name)
#由于列表是有序的,可以使用索引进行遍历
a = 0
while a < len(list_01):
    print(list_01[a])
    a += 1

for i in range(0,len(list_01),1):
    print(list_01[i])

#删除列表中所有的jack，并且将张三改成jack
list_01 = ["jack","rose","tom","lucy","jeery","jack","张三","张三","张三","张三"]
list_02 = list_01.copy()#复制一张表，副本
#遍历列表
for x in list_02:
    #x 是从 list_02 中遍历得到的元素值（字符串类型，如 "张三"），不是索引
    if x == "jack":
        list_01.remove(x)#删除操作针对原列表，即使原列表长度变化，也不会影响副本的遍历顺序
    elif x == "张三":
       z = list_01.index(x)#x是遍历list_02的索引，修改list_01的内容，需要创建01的索引
       list_01[z] = "jack" #z 是通过 list_01.index(x) 获取的索引值（整数类型），用于定位 list_01 中元素的位置
print(list_01)


"""
面试题:把[1,3,5]和[2,4,6]转换成[1,2,3,4,5,6]
max(listname);功能:返回列表中的最大值
min(listname);功能:返回列表中的最小值
"""
list_03 = [1,3,5]
list_04 = [2,4,6]
list_03.extend(list_04)#将表的内容加在一个表里
list_03.sort()#升序排序
print(list_03)









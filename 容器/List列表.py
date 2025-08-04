"""
声明list的语法:
列表名=[元素1,元素2,...,元素n];
特点：
1.有序、可变、允许重复元素、可存储任意类型数据
2.列表数据的操作,要根据索引去找值,不要根据值去找索引
3.有序的.指的是添加数据和取出数据的顺序是一致的,先进先出,后进后出的原则
4.一般情况下,一个列表中要存储相同类型的数据
"""
list_01 = [1,2,3,4,5,6,7,8,9]
"""
一、添加元素:insert/append/extend
listname.insert(index,object);  功能:在列表指定索引位置添加数据

listname.append(object);    功能:在列表末尾追加元素

listname.extend(list);  功能:向列表中添加指定列表中的元素
"""
list_01.insert(10,10)
print(list_01)

list_01.append(11)
print(list_01)

list_01.extend([12,13,14])
print(list_01)

"""
二、删除:del/pop/remove
1.listname.pop(index);  功能:根据索引删除列表中的元素
listname.pop(); 功能:删除列表中最后一个元素

2.listname.remove(object);  功能:删除列表中首次出现的元素

3.del 列表名[index];   功能:根据索引删除列表中的元素

4.listname.clear(); 功能:清空列表中的元素
"""
list_01.pop(13)
print(list_01)
list_01.pop()
print(list_01)

list_01.remove(12)
list_01.remove(5)
print(list_01)

del list_01[4]
print(list_01)

list_01.clear()
print(list_01)

"""
三、修改
listname[index]=object; 功能:根据索引修改元素
listname[index:index]=[object,object...]; 切片批量添加修改
"""
list_01[0:9] = [1,2,3,4,5,6,7,8,9,10]
print(list_01)
list_01[10:11] = [11]
print(list_01)
list_01[10] = 12
print(list_01)

"""
四、查询
1.listname[index];  功能:根据索引获取元素

2.listname.index(object);   功能:返回指定元素首次出现的索引

3.listname.index(object,start,stop);    功能:返回从指定索引开始,到指定索引处结果,首次出现元素的索引

4.listname.count(object);   功能:返回指定元素出现的次数

5.len(listname);    功能:返回列表的长度
"""

a = list_01[1]
print(a)

b = list_01.index(5,0,5)
print(b)
c = list_01.index(4)
print(c)

d = list_01.count(1)
print(d)

e = len(list_01)
print(e)

"""
五、排序
1.listname.reverse();   功能:反转排序列表(不能指定一个变量来输出！)


2.listname.sort(reverse=True);  功能:排序:reverse=True是降序排列,False是升序排列(不能指定一个变量来输出！)
,如果不写默认升序排列

3.listname.copy();  功能:复制列表(需要指定一个变量来输出)
不能指定一个变量来输出！
"""
list_01.reverse()
print(list_01)

list_01.sort()
print(list_01)
list_01.sort(reverse=True)
print(list_01)

list_02 = list_01.copy()
print(list_02)














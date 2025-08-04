"""
set集合声明的语法:
setname={元素,元素,元素};
set集合特点:
1.set集合是无序的。指的是添加元素和取出元素的顺序是不一致。
2.set集合是不允许元素重复的.
3.set集合是可变数据类型
4.因为无序，没有索引
"""
set_01 = {"tom","jack","lucy","mike","张三"}
print(set_01)#无序

set_01 = {"tom","jack","lucy","mike","张三","tom"}#不允许元素重复
print(set_01)

#添加元素
set_01.add("李华")
print(set_01)

#删除元素
set_01.remove("李华")
print(set_01)

#遍历，因为没有索引，所以不能使用while
for i in set_01:
    print(i)

#set在工作常用的用法，去重
#列表去重
list_01 = ["tom","jack","lucy","mike","张三","tom","tom","tom","tom","tom","张三","张三","张三"]
set_01 = set(list_01)#转化为set，因为set数据不能重复，实现去重
list_01 = list(set_01)
print(list_01)

#元组去重
tuple_01 = ("tom","jack","lucy","mike","张三","tom","tom","tom","tom","tom","张三","张三","张三")
set_01 = set(tuple_01)
tuple_01 = tuple(set_01)
print(tuple_01)









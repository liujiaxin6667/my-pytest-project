"""
语法结构：set:{value,value};
字典中的键统一采用 字符串 类型,值可以是 任意类型
字典中的value是可以重复的,但是键必须是唯一的
字典中获取数据,要根据键获取值,不要根据值取找键
字典中的键重复,值覆盖
id:1
name:老王
age:20
sex:男
address:隔壁
hobby:抽烟、喝酒、烫头发
"""
dict_01 = {"id":1,"name":"老王","age":20,"sex":"男","adress":"隔壁","hobby":["抽烟","喝酒","烫头"]}
"""
1.获取
dictname.get(key);    功能:根据键获取对应的值,如果键不存在,返回None
dictname[key];    功能:根据键获取对应的值,如果键不存在,会报错
"""
#根据键，获取值（1）(推荐）
value_01 = dict_01.get("age")
print(value_01)
#根据键，获取值（2）
value_02 = dict_01["age"]
print(value_02)
"""
2.修改/添加
dicntname[key]=value;   功能:如果键存在,根据键,修改值
                        如果键不存在就是向字典中添加键值对
"""
#根据键，修改值
dict_01["name"] = "tom"
print(dict_01)

#根据键，添加值
dict_01["age_0"] = "20"
print(dict_01)

"""
3.删除
dictname.pop(key);  功能:根据键删除键值对
"""
#根据键，删除键值对
dict_01.pop("age")
print(dict_01)

print("*****************************")
#遍历
for i in dict_01:#默认遍历key
    dict_value = dict_01.get(i)#根据键获取值
    print(i,dict_value)

#根据键获取值
for i in dict_01.keys():
    dict_value = dict_01.get(i)
    print(i,dict_value)

#获取列表中所有的键值对
for i,value in dict_01.items():
    print(i,value)

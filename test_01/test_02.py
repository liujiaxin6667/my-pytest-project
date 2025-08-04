#float类型转化为int
a = 12.555
print(int(a))
#str类型转化为int,str类型必须为数字字符串
b = "123456"
print(int(b))
#bool类型转化为int
c = True
print(int(c))
d = False
print(int(d))
#None类型不能转化为int

#int类型转化为float型
e = 12
print(float(e))
#str类型转化为float型
f = "123"
print(float(f))
#bool类型转化为float型
g = True
print(float(g))
h = False
print(float(h))
#None类型不能转化为float类型

#int类型转化为str类型
i = 123456
print(str(i))
#float类型转化为str类型
j = 12.321
print(str(j))
#bool类型转化为str类型
k = True
print(str(k))
l = False
print(str(l))
#None类型转化为str类型
m = None
print(str(m))

#int类型转化为bool类型
n = 123456
print(bool(n))
o = 0
print(bool(o))
p = 0
print(bool(p))
#float类型转化为bool类型
q = 31.21
print(bool(q))
r = 0.0
print(bool(r))
# str类型转化为bool类型
s = "abc"
print(bool(s))
t = " "
print(bool(t))
w = ""
print(bool(w))
#None类型转化为bool类型
x = None
print(bool(x))

#int、float、str、bool都不能转换为None类型
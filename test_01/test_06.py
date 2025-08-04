import random
a = random.randint(1,3)
b = "电脑出拳"
if a == 1:
    b = "剪刀"
elif a == 2:
    b == "石头"
elif a == 3:
    b ="布"

c = input("1 ：剪刀，2 ：石头，3 ：布，请输入：")
d = "出拳"
if c == "1":
    d = "剪刀"
elif c == "2":
    d = "石头"
elif c == "3":
    d ="布"
else:
    d ="禁止作弊！"

if (a == 1 and c == "1") or (a == 2 and c == "2") or (a == 3 and c == "3"):
    print("你出的是%s，电脑是%s，结果：平局"%(d,b))
elif(a == 1 and c == "2") or (a == 2 and c == "3") or (a == 3 and c == "1"):
    print("你出的是%s，电脑出的是%s，结果：你赢了！！！"%(d,b))
elif(a == 1 and c == "3") or (a == 2 and c == "1") or (a == 3 and c == "2"):
    print("你出的是%s，电脑出的是%s，结果：电脑赢了"%(d,b))
else:
    print(d)


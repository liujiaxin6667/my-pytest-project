a = 10
b = 20
if a > b:
    print("%s是最大值"%(a))
else:
    print("%s是最大值%s"%(b,a))


salary = input("请输入你的工资：")
money = int(salary)
if money >= 30000:
    print("大佬")
elif money < 30000 and money >= 20000:
    print("小牛")
elif money < 20000 and money >= 10000:
    print("白领")
elif money < 10000 and money >= 5000:
    print("蓝领")
elif money < 5000 and money >= 0:
    print("....")
else:
    print("本月没有工资")









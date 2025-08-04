import random#导入随机数模块
computer = random.randint(1,50)#设置一个变量，引用随机数函数
a = 1
while a <= 5:
    b = int(input(f"<猜数游戏> 你已进入第{a}次游戏，请输入数字:"))
    if b > computer:
        if a <= 4:
            print(f"你猜大了，还剩余{5-a}次机会。")
        elif a == 5:
            print("你猜大了，没有机会了")
    elif b < computer:
        if a <= 4:
            print(f"你猜小了，还剩余{5-a}次机会。")
        elif a == 5:
            print("你猜小了，没有机会了")
    else:
        print("恭喜你，猜对了！")
        break#<中断，跳出>中断当前循环，跳出循环体，继续执行循环后面的代码
        #continue <中断，继续>中断当前循环，直接进入下一次循环
    a += 1
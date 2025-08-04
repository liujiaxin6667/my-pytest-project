#1到100数字的和
a = 1
sum = 0
abc = "11"
while a <= 100:
    #循环执行语句
    sum += a
    #迭代语句
    a += 1
print(f"1到100数字和为{sum}")

#计算10的阶乘
x = 1
z = 10
while z >= 1:
    # 循环执行语句
    x *= z
    # 迭代语句
    z -= 1
print(f"10的阶乘为{x}")

#计算1-100之间偶数的和
y = 0
sum_01 = 0
while y <= 100:
    y += 1
    if y % 2 != 0:
        continue
    elif y % 2 == 0:
        sum_01 += y
print(f"1-100之间的偶数和为{sum_01}")










#九九乘法表
for i in range(1,10,1):
    for x in range(1,i+1,1):
        print(f"{x}*{i}={x*i}\t",end="")
    print()
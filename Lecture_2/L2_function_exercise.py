
# 已知一段程序可以输出四四乘法表，如何获得五五乘法表、六六乘法表、……、九九乘法表、NN乘法表？

def show_table(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(f"{i}*{j}={i*j} ", end="")
        print("")
    print("")

show_table(8)
show_table(9)
show_table(10)


# 写入文件
f = open("test_path.txt", "w")
f.write("Nice to meet you!")
f.close()

# 写到哪里去了？


# OS模块
import os

folder_name = "output"
existance = os.path.exists(folder_name)  # 判断文件/文件夹是否存在
print(existance)

if not existance:  # 若文件夹不存在则创建
    os.mkdir(folder_name)

file_name = os.path.join(folder_name, "summer.txt")  # 合并文件名
print(file_name)

f = open(file_name, "w")
f.write("I wanna go back to Tsinghua.")
f.close()

# 简要写法：若文件夹不存在则创建
if not os.path.exists("results"):
    os.mkdir(folder_name)

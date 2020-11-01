
GPA = 4.0
name = "Jack"

info = "Jack's GPA is 4.0, but he still isn't happy"  # 纯字符串

# 如果有100个人、100个数值需要显示，要把上面一行代码复制粘贴100次吗？

info1 = "%s's GPA is %0.1f, but he still isn't happy " % (name, GPA)  # 百分号格式化
info2 = "{}'s GPA is {}, but he still isn't happy".format(name, GPA)  # format 格式化
info3 = f"{name}'s GPA is {GPA}, but he still isn't happy"  # f-string 格式化


print(info)
print(info1)
print(info2)
print(info3)

for GPA in range(100):
    info3 = f"{name}'s GPA is {GPA}, but he still isn't happy"  # f-string 格式化
    print(info3)

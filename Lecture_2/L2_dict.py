

names = {"Alex": 2020010483, "Jack": 2019880789, "Tim": [2015050888, "Phd"]}

print(names["Alex"])  # 通过键访问值
# print(names["Timmy"])  # 通过键访问值
# print(names[1])  # 不可通过编号索引（实际上这等于访问不存在的键）

# print("-" * 50)

# # 常用字典操作：增删查改

# # 将新的值关联到键 "Eva" 上（新增键值对）
names["Eva"] = [2016050999, "Master"]  
print(names)
# print(names["Eva"])  # 现在可以访问键 "Eva" 了

del names["Jack"]  # 删除键为 "Jack" 的键值对
print(names)

# # 检查字典 names 是否包含键为 "Jimmy" 的键；若有则返回值；若没有，则返回0
result = names.get("Jimmy", "nonegig")
print(result)

# # 将新的值关联到键 "Eva" 上（覆盖原来的值）
names["Eva"] = [2020010001, "Professor"]  
print(names)


# {"Alex": 2020010483, "Jack": 2019880789}


# 用途举例：统计词频

text = "清华学生内卷是怎么回事呢？清华学生相信大家都很熟悉，但是清华学生内卷是怎么回事呢，下面就让小编带大家一起了解吧。\
　清华学生内卷，其实就是过度竞争，大家可能会很惊讶清华学生怎么会内卷呢？但事实就是这样，小编也感到非常惊讶。\
　　这就是关于清华学生内卷的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！"

word_list = {}
for item in text:
    if word_list.get(item, 0) == 0:
        word_list[item] = 1
    else:
        word_list[item] += 1

print(word_list)
# print(word_list["鱼"])
# print(word_list["莲"])


# """
# text = "清华学生内卷是怎么回事呢？清华学生相信大家都很熟悉，但是清华学生内卷是怎么回事呢，下面就让小编带大家一起了解吧。\
# 　　清华学生内卷，其实就是过度竞争，大家可能会很惊讶清华学生怎么会内卷呢？但事实就是这样，小编也感到非常惊讶。\
# 　　这就是关于清华学生内卷的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！"
# """

print("a")
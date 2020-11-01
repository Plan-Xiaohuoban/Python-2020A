import matplotlib.pyplot as plt

import os


# 导入pandas模块，如果不存在则安装：pip install pandas
import pandas as pd

# 使用Pandas读取excel文件
data = pd.read_excel("活动数据.xlsx")

# 如果要在图中使用中文，需要加上这两行
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号

# 若不存在则创建
folder_name = "results"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

"""
绘制各种图表。
把L3_data.ipynb直接转移了过来，稍作调整。
为了让本代码便于阅读，删去了一些中间变量和演示语句，
删去了大部分绘图控制语句，比如标题、轴标签、图例等等。
"""

# （1）直接画折线图：GPA与打卡天数的关系
plt.figure(figsize=(12, 8), dpi=400)
plt.plot(data["打卡天数"], data["GPA"])
plt.savefig(f"{folder_name}/GPA-打卡天数(折线图，未排序).jpg")

# （2）排序后画折线图：GPA与打卡天数的关系
data_sorted = data.sort_values(by="打卡天数")

plt.figure(figsize=(12, 8), dpi=400)
plt.plot(data_sorted["打卡天数"], data_sorted["GPA"])
plt.savefig(f"{folder_name}/GPA-打卡天数(折线图，排序).jpg")


# （3）画散点图：GPA与打卡天数的关系
plt.figure(figsize=(12, 8), dpi=400)
plt.scatter(data["打卡天数"], data["GPA"])
plt.savefig(f"{folder_name}/GPA-打卡天数(散点图).jpg")


# （4）使用子图画散点图：GPA与打卡天数的关系
# 步骤一：分离两类数据
data_in = data[data["备注"] == "本校学生"]
x, y = data_in["打卡天数"], data_in["GPA"]
data_out = data[data["备注"] == "外校学生"]
x2, y2 = data_out["打卡天数"], data_out["GPA"]

# 步骤二：分别画两个子图
plt.figure(figsize=(15, 8), dpi=400)
plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.subplot(1, 2, 2)
plt.scatter(x2, y2)
plt.savefig(f"{folder_name}/GPA-打卡天数(散点图，对比图).jpg")

# （5）画条形图：打卡天数的分布
plt.figure(figsize=(15, 8), dpi=400)
plt.hist(data["打卡天数"], bins=20)
plt.savefig(f"{folder_name}/GPA-打卡天数(条形图).jpg")

# （6）画折线图：GPA均值与方差随各年级的变化
# 步骤一：分离出年级
year_list = data["ID"] // 1000000

# 步骤二:新建一列
data["入学年份"] = year_list

# 步骤三：根据年级进行分类，求均值和方差，填入列表
x_list = []
ave_gpa_list = []
var_gpa_list = []
for year in range(2016, 2021):
    x_list.append(str(year))
    ave = data[data["入学年份"] == year]["GPA"].mean()
    var = data[data["入学年份"] == year]["GPA"].var()
    ave_gpa_list.append(ave)
    var_gpa_list.append(var)
ave_gpa_list


# 步骤三：把列表画出来
plt.figure(figsize=(12, 8), dpi=400)
plt.plot(x_list, ave_gpa_list, "y-*")
plt.plot(x_list, var_gpa_list, "r--*")
plt.title("成绩随年级的变化趋势")
plt.xlabel("入学年份")
plt.ylim([0, 4])
plt.grid(1)
plt.legend(["mean", "var"])
plt.savefig(f"{folder_name}/GPA均值与方差随各年级的变化(折线图).jpg")


# （7）画箱线图：GPA在各年级的分布
# 步骤一：根据年级进行分类，求均值和方差，填入列表
gpa_year_list = []
for year in range(2016, 2021):
    GPAs = data[data["入学年份"] == year]["GPA"]
    gpa_year_list.append(GPAs)

# 步骤二：画箱线图
plt.figure(figsize=(12, 8), dpi=400)
plt.boxplot(
    gpa_year_list,
    notch=False,  # 中位线处不设置凹陷
    widths=0.5,  # 设置箱体宽度
    medianprops={"color": "red"},  # 中位线设置为红色
    boxprops=dict(color="blue"),  # 箱体边框设置为蓝色
    labels=[2016, 2017, 2018, 2019, 2020],  # 设置标签
    whiskerprops={"color": "black"},  # 设置须的颜色，黑色
    capprops={"color": "green"},  # 设置箱线图顶端和末端横线的属性，颜色为绿色
)

plt.title("箱线图")
plt.xlabel("入学年份")
plt.ylabel("平均成绩")

plt.savefig(f"{folder_name}/GPA在各年级的分布(箱线图).jpg")


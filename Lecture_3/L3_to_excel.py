import pandas as pd

# 使用Pandas读取excel文件
data = pd.read_excel("活动数据.xlsx")


winners1 = data[data["打卡天数"] == 200]
winners1[["等级", "奖品"]] = ["一等奖", "一台Kindle"]

winners2 = data[(data["打卡天数"] >= 190) & (data["打卡天数"] < 200)]
winners2[["等级", "奖品"]] = ["二等奖", "一个小米手环"]

winners3 = data[(data["打卡天数"] >= 180) & (data["打卡天数"] < 190)]
winners3[["等级", "奖品"]] = ["三等奖", "一沓数学作业纸"]

# 不会覆盖的写入方法
writer = pd.ExcelWriter("output/获奖名单_自动生成.xlsx")
winners1.to_excel(writer, sheet_name="一等奖", startcol=0, index=False)
winners2.to_excel(writer, sheet_name="二等奖", startcol=0, index=False)
winners3.to_excel(writer, sheet_name="三等奖", startcol=0, index=False)
writer.save()


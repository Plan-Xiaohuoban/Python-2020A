import random
import easygui
import locale
import datetime

locale.setlocale(locale.LC_CTYPE, "chinese")
now = datetime.datetime.now()
now_str = now.strftime("%Y年%m月%d日%H时%M分")

canteen_list = [
    "紫荆园",
    "桃李园",
    "甲所",
    "澜园",
    "寓园",
    "融园",
    "清芬园",
    "观畴园",
    "芝兰园",
    "玉树园",
    "听涛园",
    "熙春园",
    "清青快餐",
]
target = random.choice(canteen_list)
message = f"现在是{now_str}，走，去吃{target}!"

image_path = f"canteens/{target}.jpg"
easygui.msgbox(msg=message, title="今天吃哪里？", ok_button="OK", image=image_path, root=None)


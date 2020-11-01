import easygui

# import random
# import easygui

# # 朴素显示
# easygui.msgbox(msg="Hello world!")

# # 输出框
num = easygui.enterbox(
    msg="请输入班级总人数", title="请输入总人数", default=30, strip=True, image=None, root=None
)
print(num)


message = f"班级总人数为{num}人"
# easygui.msgbox(msg=message, title="班级总人数", ok_button="OK", image=None, root=None)


# # 带图片
easygui.msgbox(msg=message, title="班级总人数", ok_button="OK", image="./canteens/紫荆园.jpg", root=None)


# # 自选图片
# # path = easygui.fileopenbox(msg="请选择一张图片", title="选择图片", default="*.jpg")
# # easygui.msgbox(msg=message, title="班级总人数", ok_button="OK", image=path, root=None)


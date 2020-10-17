import datetime


class Hero:
    """
    Define a class named "Hero", which will be the father class of Libai and Hanxin.
    This is a comment block surrounded by three quotation symbols.
    """

    # It looks like a function, actually it is a construction method
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def GANK(self):  # Define a "GANK" method for the class
        print("{} 级的 {} 前来支援！".format(self.level, self.name))

    def use_skill(self, number):  # Define a "use_skill" method for the class
        print("{} 级的 {} 使用了 {} 技能".format(self.level, self.name, number))


class Libai(Hero):
    """
    Libai是Hero的子类，Hero是Libai的父类（也称基类、超类）。
    继承的好处：子类获得了父类的全部功能。并能根据自己的需求覆盖父类的方法，或者扩展出新的方法。
    """

    def __init__(self, name, level):
        super().__init__(name, level)  # 调用父类（Hero类）的构造函数

    def use_skill(self, number):  # 覆盖父类的方法
        skill_list = {1: "将进酒", 2: "神来之笔", 3: "青莲剑歌"}
        if number in [1, 2, 3]:
            print(
                "{} 级的 {} 使用了 {} 技能：{}".format(
                    self.level, self.name, number, skill_list[number]
                )
            )

    def StealTower(self):  # 扩展出新的方法
        print("{} 级的 {} 在偷塔!".format(self.level, self.name))


def show_skills(hero):
    for i in range(4):
        hero.use_skill(i)


def show_time():
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("The current time is", now_str)


if __name__ == "__main__":
    show_time()
    fighter = Libai("李白", 13)
    fighter.GANK()
    show_skills(fighter)


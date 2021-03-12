class Hero:
    def __init__(self, name, gender, height, weight, age):
        self.heroName = name
        self.heroGender = gender
        self.heroHeigh = height
        self.heroWeight = weight
        self.heroAge = age
def showInfo():
    print(x.heroName,x.heroGender)
    print(x2)
    print(x3)

x = Hero("車車", "女", "160","47","15")
x2 = Hero("刺蛇", "男","177","65","23")
x3 = Hero("嘎嘎", "女","156","52","13")
showInfo()




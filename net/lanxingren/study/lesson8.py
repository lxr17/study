class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, class_name):
        print("%s正在学习%s" % (self.name, class_name))

    # watch_movie表示方法是公开的
    # _watch_movie表示方法是protected的
    # __watch_movie表示方法是私有的
    def watch_movie(self):
        if self.age > 18:
            print("正在看美丽人生")
        else:
            print("正在看熊出没")

    def __xxx(self):
        print(self)


def main():
    stu1 = Student("张三", 17)
    stu1.watch_movie()

    stu2 = Student("我", 19)
    stu2.watch_movie()
    stu2.study("科学")
    # stu2._Student__xxx() 此方法可以调用私有方法


class Clock:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def run(self):
        if self.s == 59:
            self.s = 0
            if self.m == 59:
                self.m = 0
                if self.h == 23:
                    self.h = 0
                else:
                    self.h += 1
            else:
                self.m += 1
        else:
            self.s += 1


def test_clock():
    import time

    clock1 = Clock(23, 59, 59)
    clock2 = Clock(11, 23, 54)

    for i in range(100):
        print("现在时刻：%s:%s:%s" % (clock1.h, clock1.m, clock1.s))
        clock1.run()
        time.sleep(1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

    # 该方法相当于是一个Java里的toString方法
    def __str__(self):
        return "x={0}, y={1}".format(self.x, self.y)


if __name__ == '__main__':
    # main()
    # test_clock()
    point1 = Point(1, 2)
    point2 = Point(2, 3)

    print(point1.distance(point2))
    print(point2)

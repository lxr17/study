# 水仙花数
# for i in range(100, 1000):
#     a = i // 100
#     b = (i - a * 100) // 10
#     c = i % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)


# 百钱白鸡问题
# for z in range(0, 301, 3):
#     for x in range(21):
#         m = (100 - 5 * x - z / 3) % 3
#         y = (100 - 5 * x - z / 3) // 3
#         if m == 0 and y >= 0 and x + y + z == 100:
#             print("公鸡%d只，母鸡%d只，小鸡%d只" % (x, y, z))


# CRAPS赌博游戏    最终的结果是赌博害人！！！
# import random
#
# a, b = 0, 0
# first = 0
# count = 0
#
# amount = 100
# goon = "1"
#
# while goon == "1":
#     a = random.randint(1, 6)
#     b = random.randint(1, 6)
#     count += 1
#
#     # 第一次
#     if count == 1:
#         first = a + b
#         if first == 7 or first == 11:
#             print("本次掷骰子结果为：%d、%d，共%d点，玩家胜！" % (a, b, a + b))
#             amount += 10
#             goon = str(input("您当前的总金额为" + str(amount) + "，是否继续？继续请输入1，否则输入0:"))
#         elif first == 2 or first == 3 or first == 12:
#             print("本次掷骰子结果为：%d、%d，共%d点，庄家胜！" % (a, b, a + b))
#             amount -= 10
#             goon = str(input("您当前的总金额为" + str(amount) + "，是否继续？继续请输入1，否则输入0:"))
#         else:
#             print("本次掷骰子结果为：%d、%d，共%d点，无人胜出。" % (a, b, a + b))
#             goon = str(input("您当前的总金额为" + str(amount) + "，是否继续？继续请输入1，否则输入0:"))
#     else:
#         if a + b == 7:
#             print("本次掷骰子结果为：%d、%d，共%d点，庄家胜！" % (a, b, a + b))
#             amount -= 10
#             goon = str(input("您当前的总金额为" + str(amount) + "，是否继续？继续请输入1，否则输入0:"))
#         elif a + b == first:
#             print("本次掷骰子结果为：%d、%d，共%d点，玩家胜！" % (a, b, a + b))
#             amount += 10
#             goon = str(input("您当前的总金额为" + str(amount) + "，是否继续？继续请输入1，否则输入0:"))
#         else:
#             print("本次掷骰子结果为：%d、%d，共%d点，无人胜出。" % (a, b, a + b))
#             goon = str(input("您当前的总金额为" + str(amount) + "，是否继续？继续请输入1，否则输入0:"))


## 生成斐波那契数列
# a = 1
# b = 1
# while b < 1000:
#     print(a)
#     print(b)
#     a = a + b
#     b = a + b


## 找出所有的完美数
# import time
#
# time1 = time.time()
# for num in range(2, 10001):
#     s = 1
#     for i in range(2, num):
#         if num % i == 0:
#             s += num // i
#
#     if s == num:
#         print(num)
#
# time2 = time.time()
#
# print("一共花了%d秒的时间" % (time2 - time1))


## 找出100以内的所有素数
# for i in range(2, 101):
#     if i == 2:
#         print(2)
#         continue
#
#     isSushu = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             isSushu = False
#             break
#
#     if isSushu:
#         print(i)


## 对于任意输入的数进行分解质因数
n = int(input("请输入一个整数："))
over = False
while not over:
    for i in range(2, n + 1):
        if i == n:
            over = True
            print(i, end="")
            break

        if n % i == 0:
            print(i, end="\t")
            n = n // i
            break

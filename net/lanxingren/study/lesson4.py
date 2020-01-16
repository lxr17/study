# s = 0
# step = 1
# for x in range(0, 101, step):  # step变化不影响这个序列
#     s = s + x
#     step += 1
#     print(x)


# sum1 = 0
# for x in range(11):
#     if x % 2 == 0:
#         sum1 += x
# print(sum1)


# import random
#
# ans = random.randint(2, 100)
#
# guess = 0
# count = 0
# while guess != ans:
#     guess = int(input("请输入你要猜的数字："))
#
#     count += 1
#
#     if guess < ans:
#         print("太小了")
#     elif guess > ans:
#         print("太大了")
#     else:
#         print("猜对了！")
#
# print("你总共猜了%d次" % count)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%d * %d = %d" % (i, j, i * j))


# import math
#
# a = int(input("请输入一个整数："))
#
# b = int(math.sqrt(a))
#
# isSushu = True
# for x in range(2, b + 1):
#     if a % x == 0:
#         isSushu = False
#         print("%d = %d * %d" % (a, x, a / x))
#         break
#
# if isSushu:
#     print("%d是一个素数。" % a)


# 计算器直接用python3来计算


# 计算最大公约数和最小公倍数
# a = int(input())
# b = int(input())
#
# x1 = a
# while True:
#     if a % x1 == 0 and b % x1 == 0:
#         print("最大公约数为%d" % x1)
#         print("最大公倍数为%d" % (a * b / x1))
#         break
#     else:
#         x1 -= 1


# 打印三角形
# for i in range(1, 8):
#     for j in range(i):
#         print("*", end="")
#     print("")

# for i in range(1, 8):
#     for j in range(7):
#         if i >= 7 - j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")

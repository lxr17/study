"""
作者：我
"""

# a = str(input("请输入用户名："))
# b = str(input("请输入密码："))
# a = "admin"
# b = "password"
#
# if (a is "admin") and (b is "password"):
#     print("登陆成功！")
# else:
#     print("登录失败！")

# a = float(input("请输入一个整数："))
#
# if a > 1:
#     b = 3 * a - 5
# elif -1 <= a <= 1:
#     b = a + 2
# else:
#     b = 5 * a + 3
#
# print("答案是%.2f" % b)

# a = int(input("请输入一个整数:"))
#
# if a % 2 == 0:
#     print("%d是一个偶数。" % a)
# else:
#     print("%d是一个奇数。" % a)


# 输入一个数字，首先判断位数等于3，然后判断各个数字相加是不是等于9
a = str(input("请输入一个数字："))

if len(a) != 3:
    print("输入的数字无效。")
else:
    a1 = int(a) // 100
    a2 = (int(a) - a1 * 100) // 10
    a3 = int(a) % 10

    if a1 + a2 + a3 == 9:
        print("这个数字是合规的。")
    else:
        print("这个数字是不合规的。")

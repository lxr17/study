# 输出代码本身的算法


# 定义求阶乘的方法
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# a = int(input("请输入一个整数："))
# print("%d!=%d" % (a, factorial(a)))


# 函数的参数
# from random import randint
#
#
# def roll_dice(n=2):
#     s = 0
#
#     for i in range(n):
#         s += randint(1, 6)
#
#     return s
#
#
# print(roll_dice())
# print(roll_dice(3))
#
#
# def add_sum(a=0, b=0, c=0):
#     return a + b + c
#
#
# print(add_sum())
# print(add_sum(b=1))
# print(add_sum(a=1, c=5))
#
#
# def add(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(add(1, 2, 3, 4, 5, 6, 7))


# 同名函数会怎样, 后者会覆盖前者
# def foo():
#     print("hello, world")
#
#
# def foo():
#     print("hello, python")
#
#
# foo()


# Python中一个文件就代表一个模块，可以导入
# from net.lanxingren.study.lesson6_1 import foo
#
# foo()


# # 最大公约数
# def gcd(x, y):
#     for _ in range(x, 0, -1):
#         if x % _ == 0 and y % _ == 0:
#             return _
#
#
# # 最小公倍数
# def lcm(x, y):
#     _ = x
#     while not (_ % x == 0 and _ % y == 0):
#         _ += 1
#     else:
#         return _
#
#
# if __name__ == '__main__':
#     x = int(input("第一个数："))
#     y = int(input("第二个数："))
#
#     print("最大公约数为：%d" % gcd(x, y))
#     print("最小公倍数为：%d" % lcm(x, y))


# 回文数
# def is_palindrome(num):
#     a = 0
#     n = num
#     while n > 0:
#         a = a * 10 + n % 10
#         n = n // 10
#
#     return a == num
#
#
# if __name__ == '__main__':
#     a = int(input("请输入一个数字:"))
#     print("该数字是回文数吗？%s" % is_palindrome(a))


# 判断是不是素数
# def is_prime(num):
#     is_prime = True
#     for _ in range(2, int(num ** 0.5) + 1):
#         if num % _ == 0:
#             is_prime = False
#             break
#
#     return is_prime
#
#
# if __name__ == '__main__':
#     a = int(input("请输入一个整数："))
#     print("%d是素数吗？%s" % (a, is_prime(a)))


# 计算第n位斐波那契数列的值
# def fbnq(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fbnq(n - 1) + fbnq(n - 2)
#
#
# if __name__ == '__main__':
#     a = int(input("请输入一个整数："))
#     print("第%d位斐波那契数列的值为：%d" % (a, fbnq(a)))


# 变量的作用域(nonlocal与global的使用，一个是让变量沿用上一级的，一个是让变量是全局的)
# def aaa():
#     a = 100
#
#     def bbb():
#         a = 200
#
#         def ccc():
#             nonlocal a
#             a = 300
#
#         ccc()
#         print(a)
#
#     bbb()
#
#     print(a)
#
#
# if __name__ == '__main__':
#     aaa()

def main():
    # TODO
    return


if __name__ == '__main__':
    main()

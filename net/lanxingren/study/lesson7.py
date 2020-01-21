# s1 = "hello, world"
# s2 = 'hello, world'
# s3 = '''
# hello
# world
# '''
# print(s1, s2, s3, sep="_", end="")

# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u4f55\u91d1\u534e'
# print(s1, s2)

# s1 = "hello" * 3
# print(s1)
# s2 = "world" + s1
# print(s2)
# print("hell" in s2)
# print("" in s2)

# str = "abcdefghijklmnopqrstuvwxyz1234567890"
# ::后面代表的是step
# print(str[10:-20])
# print(str[::2])
# print(str[1::-1])

# str = "hello" * 3 + "world"
# print(len(str))
# print(str.isascii())
# print(str.capitalize())
# print(str.title())
# print(str.center(30, "*"))
#
# for _ in range(10):
#     str = "a" * (_ + 1)
#     print(str.ljust(10, "*"))

# 格式化字符串
# str = "{0} + {1} = {2}"
# print(str.format(4, 5, 9))

# a = [1, None, "字符串", True] * 3
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
#
# for ele in a:
#     print(type(ele))
#
# a.remove(None)

# a = list("0123456789")
# for item in a:
#     a.remove(item)
# print(a)

# a = list("23241231313131123123")
# index = 0
# while "3" in a:
#     a.remove("3")
# print(a)

# a = list("0123456789")
# i = 0
# for item in a[i:]:
#     a.remove(item)
#     i = i + 1
# print(a)

# b = list("137347374783832837848383")
# j = 0
# for item1 in b[j:]:
#     print(item1)
#     if item1 == '3':
#         b.remove(item1)
#     j = j + 1
# print(b)

# a = list("0123456789")
# i = 0
# for item in a[i:]:
#     a.remove(item)
#     i = i + 1
# print(a)

# c = "   1341   2123 "
# print(c.split(None))

# import sys
#
# a = (1, 2)
# print(sys.getsizeof(a))

# import sys
#
# f = [x ** 2 for x in range(1, 1000)]
# print(f.__sizeof__())
# print(sys.getsizeof(f))

# t = ("这是一个元祖", True, None)
# for item in t:
#     print(item)
#
# print(t)
# print(list(t))
#
# l = ["这是一个列表", False, 3, None]
# print(tuple(l))

# set1 = {1, 2, 3, 4, 5, None}
#
# print(set1)
#
# print(set(range(10)), set1)
#
# set1.update([11, 12])
# print(set1)
# print(set1.pop())

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# # 判断子集和父集
# print(set1 > set2)

# Python中没有出现任何分号吗?
# 字典
# score = {None: None, 1: {2}}
# print(score)

# zip用来把两个一维结构变为二位结构
# item = dict(zip("1", "123"))
# zzz = {1, 2, 3}
# print(zzz)
# print(item)
#
# item.update(你好="大家好", q=2)
#
# print(item)

# import os
# import time
#
#
# def main():
#     s = "北京欢迎你......."
#     while True:
#         os.system('clear')
#         print(s)
#         s = s[1:] + s[:1]
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     main()

# tuple1 = ((1, 2), [2, 3])
#
# tuple1[1][0] = 4
#
# print(hash({1, 2}))
# print(tuple1)

# set1 = {1, 2}
# set1.update((3, 4))
#
# print(set1)

# set2 = {1, 2, 3, 2, 1}
# set2.update([5])
# print(set2)

# import random
#
# def generator_code(n=4):
#     str = "abcdefghijklmnopqrstuvwxyz0123456789"
#     ans = ""
#     while n > 0:
#         index = random.randint(0, len(str) - 1)
#         ans = ans + str[index]
#         n -= 1
#
#     return ans
#
#
# if __name__ == '__main__':
#     n = int(input("请输入位数："))
#     print(generator_code(n))


# def get_suffix(str=""):
#     a = str.split(".")
#     return a[len(a) - 1]
#
#
# if __name__ == '__main__':
#     a = str(input("请输入一个文件名："))
#     print(get_suffix(a))

# 计算最大的两个数
# def max2(x=[]):
#     m1 = x[0]
#     m2 = x[0]
#
#     for i in range(1, len(x)):
#         if x[i] < m1:
#             if x[i] >= m2:
#                 m2 = x[i]
#         else:
#             m2 = m1
#             m1 = x[i]
#
#     return m1, m2
#
#
# if __name__ == '__main__':
#     list1 = [10, 2, 3, 11, 1, 6, 7, 8]
#     print(max2(list1))

# set1 = {"1"}
# set1.update('今天不是一个好日子')
# print(set1)


# def is_lunar(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def count_day(year, month, day):
#     list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     s = 0
#     for i in range(1, month):
#         if i == 2:
#             if is_lunar(year):
#                 s += 29
#             else:
#                 s += 28
#         else:
#             s += list[i - 1]
#     return s + day
#
#
# if __name__ == '__main__':
#     number = count_day(2020, 3, 21)
#     print(number)

# class Man():
#     def eat(self):
#         print("hello")
#
#
# xiao_ming = Man()
# xiao_ming.eat()
# Man.eat(xiao_ming)
#
# def a():
#     print("a")
#     b()
#
# def b():
#     print("b")
#
# import dis
# dis.dis(a)


# class foo():
#     __x = "20"
#
# class foo2(foo):
#     def __init__(self):
#         print(self.__x)
#
# a = foo()
# b = foo2()
# import sys
# print(sys.argv)


#

with open("a.txt", "w", encoding="gbk") as f:
    f.write("你好")
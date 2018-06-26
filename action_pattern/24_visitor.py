#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:24_visitor.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 访问者模式 首先有访问者和被访问元素，然后通过一个对象结构来存储所有的被访问元素
# 在被访问元素中提前定义好各个访问者访问时的操作


class Visitor(object):
    """
    抽象访问者
    为每个元素提供一个访问方法
    """

    def visit(self, acceptor, *args, **kwargs):
        meth = None
        for cls in acceptor.__class__.__mro__:       # 从所有的类和继承类去找名字
            meth_name = "visit_{}".format(cls.__name__)
            meth = getattr(self, meth_name, None)
            if meth:
                break
        if not meth:
            return self.general_visit(acceptor, *args, **kwargs)  # 没找到就调用公共访问方法
        return meth(acceptor, *args, **kwargs)

    @staticmethod
    def general_visit(acceptor, *args, **kwargs):
        """
        对visitor没有具体定义访问方法的类提供公共访问方法
        :param acceptor:
        :param args:
        :param kwargs:
        :return:
        """
        print("we visit {}".format(acceptor.name))


class UserVisitor(Visitor):
    """
    具体访问者
    """
    def visit_A(self, acceptor, *args, **kwargs):
        print("we visit A specially, name:{}".format(acceptor.name))


class ObjectStructure(object):
    """
    对象结构，用于存储元素
    """
    def __init__(self):
        self._elements = []

    def add_elements(self, e):
        self._elements.append(e)

    def remove_elements(self, e):
        self._elements.remove(e)

    def accept(self, visitor, *args, **kwargs):
        for e in self._elements:
            e.accept(visitor, *args, **kwargs)


class User(object):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor, *args, **kwargs):
        return visitor.visit(self, *args, **kwargs)


class A(User):
    pass


class B(User):
    pass


if __name__ == '__main__':
    xiaohua = A("小花")
    dahua = A("大花")
    xiaoli = B("小李")
    visitor = UserVisitor()
    users = ObjectStructure()
    users.add_elements(xiaohua)
    users.add_elements(xiaoli)
    users.accept(visitor)

    visitor.visit(dahua)
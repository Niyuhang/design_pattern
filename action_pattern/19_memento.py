#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:19_memento.py

    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 备忘录模式，通过一个备忘录来存储内部状态，然后通过一个管理者来进行备忘录的保存


class Memento(object):
    """
    备忘录类
    """

    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Chess(object):
    """
    原声类 可以保存状态，生成备忘录，并且根据一个备忘录修改状态
    """
    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_name(self, name):
        self._name = name

    def display(self):
        print("{name} is in ({x}, {y})".format(name=self._name, x=self._x, y=self._y))

    def save(self):
        return Memento(self._name, self._x, self._y)

    def restore(self, mem: Memento):
        self.set_name(mem.name)
        self.set_x(mem.x)
        self.set_y(mem.y)


class ChessCaretaker(object):
    """
    备忘录管理
    """
    def __init__(self):
        self.mem = None

    def set_memento(self, memento: Memento):
        self.mem = memento

    def get_memento(self):
        if not self.mem:
            raise ValueError("备忘录为空")
        return self.mem


if __name__ == '__main__':
    chess = Chess("测试", 1, 2)
    chess.display()
    mc = ChessCaretaker()
    mc.set_memento(chess.save())
    chess.set_x(23)
    chess.display()
    print("######悔棋了######")
    chess.restore(mc.get_memento())
    chess.display()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:12_flyweight.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 享元模式，享元模式主要利用一个享元池来进行对象的共享，
# 关键在于要有一个抽象的共享类型，然后要有一个享元工厂来进行管理，
# 包括在不存在某个享元的时候进行创建，以及已经有的从享元池中拿出
# 节约内存，提高性能

from functools import wraps


def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not instance.get(cls):
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


class Position(object):
    """
    棋子外部状态
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def display(self):
        print("当前棋子在{},{}".format(self._x, self._y))


class Chess(object):
    """
    抽象享元类
    """
    color = ""

    def get_color(self):
        print(self.color)

    def display(self, x, y):
        pos = Position(x, y)
        pos.display()


class BlackChess(Chess):
    def __init__(self):
        self.color = "black"


class WhiteChess(Chess):
    def __init__(self):
        self.color = "white"


@singleton
class FlyWeightFactory():
    """
    利用单例模式创建的简单工厂
    """
    flyweight_pool = {}  # 享元池，用来存放共享对象

    def create_chess(self, color):
        if color not in self.flyweight_pool.keys():
            if color == "black":
                chess = BlackChess()
            elif color == "white":
                chess = WhiteChess()
            else:
                return
            self.flyweight_pool[color] = chess
        else:
            chess = self.flyweight_pool[color]
        return chess


flyfac = FlyWeightFactory()
chess1 = flyfac.create_chess("black")
chess2 = flyfac.create_chess("black")
chess3 = flyfac.create_chess("black")
chess1.display(2, 3)
chess2.display(3, 4)


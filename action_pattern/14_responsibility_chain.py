#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:14_responsibility_chain.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 职责链模式讲请求的发送者和接受者分开，并且所有的接受者为一条链，
# 所有人都有机会去处理这条数据


class Chief(object):
    """
    抽象处理类
    """
    def handle_food(self, food):
        pass

    def successor(self, chief):
        self.nex = chief


class Level1Chief(Chief):
    def handle_food(self, food):
        if food.price < 50:
            print("level1 handle food")
        else:
            self.nex.handle_food(food)


class Level2Chief(Chief):
    def handle_food(self, food):
        if food.price < 100:
            print("level2 handle food")
        else:
            self.nex.handle_food(food)


class Level3Chief(Chief):
    def handle_food(self, food):
        if food.price < 200:
            print("level3 handle food")
        else:
            self.nex.handle_food(food)


class Food(object):
    def __init__(self, price):
        self.price = price


if __name__ == '__main__':
    le1 = Level1Chief()
    le2 = Level2Chief()
    le3 = Level3Chief()
    le1.successor(le2)
    le2.successor(le3)
    food = Food(40)
    le1.handle_food(food)

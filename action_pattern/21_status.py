#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:21_status.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 状态模式 状态模式是将一个对象的状态变化的业务封装成一个状态类，并且利用一个环境来控制状态转移
# 这样子增加一个状态时，只需要增加一个状态类

from abc import ABCMeta, abstractmethod


class Man(object):
    """
    状态上下文，用来持有状态，并且进行状态的转移
    """
    def __init__(self, name):
        self.name = name
        self._status = Full(self)

    def set_status(self, status):
        self._status = status(self)

    def handle(self):
        self._status.handle()


class Status(object, metaclass=ABCMeta):
    """
    抽象状态类
    """
    @abstractmethod
    def handle(self):
        pass


class Hungry(Status):

    def __init__(self, man):
        self.man = man

    def _eat(self):
        print("{} eat food".format(self.man.name))

    def handle(self):
        print("i'm hungry")
        self._eat()

    @staticmethod
    def eat():
        print("i want to eat")


class Full(Status):
    def __init__(self, man):
        self.man = man

    def handle(self):
        print("i don't want to eat any food more")


if __name__ == '__main__':
    man1 = Man("小李")
    man1.handle()
    man1.set_status(Hungry)
    man1.handle()

    man2 = Man("小花")
    man2.set_status(Hungry)
    man2.handle()

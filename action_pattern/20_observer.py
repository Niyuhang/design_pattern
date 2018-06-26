#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:20_observer.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 观察者模式 观察者模式包含一个subject 观察目标，观察目标会注册很多的观察者，
# 当观察目标发生改变就会通知所有的观察者进行相应改变，好处是挂查目标不需要知道有多少依赖他的对象
# 并且也不关心依赖对象具体怎么做，而且观察者可以在不同的观察目标下

from abc import ABCMeta, abstractmethod


class Subject(object):
    """
    抽象观察目标
    """
    def __init__(self):
        self._observers = []

    def attach(self, ob):
        self._observers.append(ob)

    def detach(self, ob):
        self._observers.remove(ob)

    def notice(self, *args, **kwargs):
        """
        通知所有的观察者
        :return:
        """
        for ob in self._observers:
            ob.update(*args, **kwargs)


class Observer(object, metaclass=ABCMeta):
    """
    抽象观察者
    """

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Light(Subject):
    pass


class CarA(Observer):
    def update(self, *args, **kwargs):
        light = args[0]
        if light == "g":
            print("go")
        elif light == "r":
            print("闯红灯继续跑")


class CarB(Observer):
    def update(self, *args, **kwargs):
        light = args[0]
        if light == "g":
            print("let's go")
        elif light == "r":
            print("不闯红灯停下来")


if __name__ == '__main__':
    grd_light = Light()
    car_a = CarA()
    car_b = CarB()
    grd_light.attach(car_a)
    grd_light.attach(car_b)
    grd_light.notice("r")
    grd_light.notice("g")



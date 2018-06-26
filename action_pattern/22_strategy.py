#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:22_strategy.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 策略模式 将算法的定义和使用分离开，将一个算法的具体定义封装成一个具体的策略，
# 然后通过一个上下文环境进行策略的使用


class Context(object):
    """
    上下文环境
    """
    @staticmethod
    def work(strategy, *args, **kwargs):
        strategy = strategy()
        strategy.execute(*args, **kwargs)


class Strategy(object):
    """
    抽象策略类
    """
    def execute(self, *args, **kwargs):
        pass


class MondayStrategy(Strategy):
    def execute(self, *args, **kwargs):
        print("第一天 好好工作")


class FridayStrategy(Strategy):
    def execute(self, *args, **kwargs):
        print("周五了要下班了")


class SundayStrategy(Strategy):
    def execute(self, *args, **kwargs):
        print("好好休息")


if __name__ == '__main__':
    Context.work(SundayStrategy)
    Context.work(MondayStrategy)

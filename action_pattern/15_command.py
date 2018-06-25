#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:15_command.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 命令模式，
# 命令模式通过将操作封装成一些列的命令，只要想Invoker注入不同的命令，就可以实现一个Invoker来处理不同的请求
# 当命令执行时，还会有一个接受者，用来实现具体的业务代码
# 可以有效的实现命令的新增
# 为了更好的实现单一指责，command并不会参与具体的业务代码时候，而完全让一个receiver进行业务代码的实现，
# 也同时为了receiver的复用

from abc import ABCMeta, abstractmethod


class Invoker(object):
    """
    抽象命令发送者，接受一个命令作为参数
    """
    def __init__(self, command):
        self.command = command

    def run(self, *args, **kwargs):
        self.command.execute(*args, **kwargs)


class Command(object, metaclass=ABCMeta):
    """
    抽象命令类
    """
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class AddReceiver(object):

    def opperation(self):
        print("we add the num")


class MinusReceiver(object):

    def opperation(self):
        print("we minus the num")


class AddCommand(Command):
    rec = AddReceiver()

    def execute(self, *args, **kwargs):
        self.rec.opperation()


class MinusCommand(Command):
    rec = MinusReceiver()

    def execute(self, *args, **kwargs):
        self.rec.opperation()


if __name__ == '__main__':
    addinvoker = Invoker(AddCommand())
    addinvoker.run()

    minusinvoker = Invoker(MinusCommand())
    minusinvoker.run()
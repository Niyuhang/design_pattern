#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:17_iterator.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 迭代器模式
# python 的for . in .. 语句， in会直接调用对象的iter方法，返回一个迭代器
# 对一个对象进行遍历


class NList(object):
    i = 0

    def __init__(self, *args):
        self._list = list(args)

    def __iter__(self):
        return self

    def __next__(self):
        length = len(self._list)
        if self.i == length:
            raise StopIteration
        value = self._list[self.i]
        self.i += 1
        return value

    @property
    def value(self):
        return self._list

    def append(self, value):
        self._list.append(value)


a = iter(NList(1, 2, 3, 4))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:13_proxy.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 代理模式，代理模式是当客户端并不想直接访问一个对象时，
# 采用第三方对象来进行代理访问，使用代理模式，可以使得客户端自己不需要去控制对象，
# 还可以在访问真实对象前，进行控制。


class AbstractSubject(object):
    def walk(self):
        pass


class Subject(AbstractSubject):
    def walk(self):
        print("walk")


class SubProxy(AbstractSubject):
    def _pre_walk(self):
        print("hello")

    def _after_walk(self):
        print("sleep")

    def walk(self):
        self._pre_walk()
        sub = Subject()
        sub.walk()
        self._after_walk()

a = SubProxy()
a.walk()
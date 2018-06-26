#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:23_template.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 模版方法，可以在父类定义好一个模版，然后在子类中进行拓展，
# 还可以通过一个钩子函数，返回一个bool值，来控制父类写好的方法的执行


class TemplateMethod(object):

    def __init__(self):
        self.value = "lla"

    def calculate(self):
        pass

    def value_print(self):
        if self.is_print():
            print("the result for this method is {}".format(self.value))

    @staticmethod
    def is_print():
        """
        钩子方法，通过钩子来控制父类的方法
        :return:
        """
        return False

    def work(self):
        self.calculate()
        self.value_print()


class SlowMethod(TemplateMethod):
    def calculate(self):
        print("calculate slowly")
        self.value = "233"

    @staticmethod
    def is_print():
        return True


if __name__ == '__main__':
    me1 = TemplateMethod()
    me1.work()
    me2 = SlowMethod()
    me2.work()
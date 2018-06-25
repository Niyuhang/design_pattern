#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:16_Interpreter.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""

# 解释器模式 定义一个语言语法，并且用相应的解释器进行解析
# 复杂度高


class Context(object):
    """
    上下文，包含一些全局信息
    """


class Expression(object):
    """
    语法类
    """
    pass


class TerminalExpression(Expression):
    """
    终结类语法
    """
    pass


class NonTerminalExpression(Expression):
    """
    非终结类语法
    """
    pass


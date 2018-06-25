#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable = line-too-long
"""
    @FIle:18_Mediator.py
    
    ~~~~~~~~~~~
    :copyright: (c) 2017 by the eigen.
    :license: BSD, see LICENSE for more details.
"""
# 中介者模式 与外观模式和代理模式有点相似，但是每个还是有点不同
# 首先外观模式，是一个高级接口，下面管理者很多的子系统
# 而代理模式则是给一个第三方对象提供了一个代理对象，客户端只需要操作代理对象，可以说是单向的
# 中介者模式，给双方对象的调用提供了一个中介者，协调多个对象


class Mediator(object):
    """
    抽象中介者
    """
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    @property
    def users(self):
        return self._users

    def operation(self, *args):
        pass


class UserMediator(Mediator):
    def operation(self, user):
        if isinstance(user, AdminUser):
            [us.operation() for us in self._users if isinstance(us, EditorUser)
                                                  or isinstance(us, HrUser)]
        if isinstance(user, HrUser):
            [us.operation() for us in self._users if isinstance(us, EditorUser)]


class User(object):
    """
    抽象用户类，所有用户类需要两个方法，
    一个是当中介者通知时的自身操作，
    一个是和中介者的通讯
    """
    def __init__(self, mediator):
        self.mediator = mediator
        mediator.add_user(self)

    def operation(self):
        """
        自身相关操作
        :return:
        """
        pass

    def communicate(self):
        """
        与中介者通讯
        :return:
        """
        self.mediator.operation(self)


class AdminUser(User):
    def operation(self):
        print("admin work")


class HrUser(User):
    def operation(self):
        print("hr work")


class EditorUser(User):
    def operation(self):
        print("editor work")


if __name__ == '__main__':
    mediator = UserMediator()
    admin = AdminUser(mediator)
    hr1 = HrUser(mediator)
    hr2 = HrUser(mediator)
    editor1 = EditorUser(mediator)
    editor2 = EditorUser(mediator)

    hr1.communicate()


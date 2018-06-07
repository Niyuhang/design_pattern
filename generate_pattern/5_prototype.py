# 原型模式，对于一些类的重复出现，可以进行对这些类的拷贝，使得可以在这个类的基础上进行修改

import copy


class Prototype(object):
    def clone(self, **kwargs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(**kwargs)
        return obj


class ApplePrototype(Prototype):
    pass


if __name__ == '__main__':
    apple = ApplePrototype()
    apple_a = apple.clone(value_a="value_a")
    apple_b = apple_a.clone(value_b="value_b")
    print(apple_a.__dict__)
    print(apple_b.__dict__)
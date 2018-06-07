# 单例模式，在一次程序启动中，如果有些对象的资源和一些条件不变，就没有必要在开一个实例，
# 使用单例模式可以节省资源


# 第一种方法，利用__new__
from functools import wraps


class SingletonA:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonA, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# 第二种使用类装饰器
def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        print(instance)
        if not instance.get(cls):
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


# a = SingletonA()
# b = SingletonA()
# print(id(a) == id(b))


@singleton
class A:
    def __init__(self, *args):
        pass


a = A(2, 3)
a2 = A(3, 4)
print(id(a) == id(a2))
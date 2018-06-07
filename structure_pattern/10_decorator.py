# 装饰模式 是指在原有的基础上进行功能的扩展，在python当中，最明显的就是装饰器
# 装饰器使用了闭包的概念， 传递了自由变量f

from functools import wraps


def decorator(f):
    """自由变量f"""
    print("this is the first time")
    @wraps(f)
    def inner(*args, **kwargs):
        print("hello world")
        return f(*args, **kwargs)
    return inner


@decorator
def func():
    print("hello you")

# 在函数定义的时候，装饰器inner函数外的执行，返回了inner函数
# 等同于 func = decorator(func)


if __name__ == '__main__':
    func()
    func()


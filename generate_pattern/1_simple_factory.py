# 简单工厂，所有的产品都继承自抽象的产品类，这样子在新增同类的产品时候我们就不需要
# 对原有产品进行修改
# 接着创建一个工厂类，由客户端传入创建参数，而客户端自身不需要了解创建的细节
# 两种方式来存放所有的水果类
# 1.直接利用globals
# 2.利用装饰器来获取所有

Fruits = {}


def fruits(f):
    Fruits[f.__name__] = f
    return f


class Fruit():
    """
    水果抽象基类
    """
    def roll(self):
        """
        水果滚啊滚
        :return:
        """
        print("滚啊滚")


@fruits
class Apple(Fruit):
    """苹果具体类"""
    pass


@fruits
class Orange(Fruit):
    pass


class FruitFactory():
    # 利用静态方法的制造方法
    @staticmethod
    def build_fruit(fruit_type: str):
        fruit = fruit_type.capitalize()
        if fruit not in Fruits.keys():
            raise ValueError
        else:
            return Fruits[fruit]()


# fruit = FruitFactory.build_fruit("mango")
orange = FruitFactory.build_fruit("orange")
orange.roll()
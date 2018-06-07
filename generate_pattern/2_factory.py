# 工厂模式，与简单工厂不同，简单工厂只有一个共同过的工厂，根据传入的不同参数，来决定生产不同的产品
# 而工厂模式则是每一个具体的产品有一个相应的工厂类，工厂类的职责更加单一


class FruitFactory():
    """抽象的工厂类"""
    def create_fruit(self):
        print("hello")


class OrangeFactory():
    """具体的橘子工厂类"""
    def create_fruit(self):
        return Orange()


class AppleFactory():
    def create_fruit(self):
        return Apple()


class Fruit():
    """抽象水果类"""
    pass


class Orange(Fruit):
    pass


class Apple(Fruit):
    pass


if __name__ == '__main__':
    today_fruit = OrangeFactory().create_fruit()
    print(today_fruit)
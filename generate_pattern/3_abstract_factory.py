# 与工厂方法不同，抽象工厂方法用于一组产品的生成，
# 当我们由一组类似产品时，使用工厂方法就需要创建很多的产品类和工厂类
# 而使用抽象工厂可以更好的生成一系列同一等级的产品


# 一组等级的苹果
class Apple():
    pass


class AppleA(Apple):
    pass


class AppleB(Apple):
    pass


class AppleC(Apple):
    pass


# 一组等级的香蕉
class Banana():
    pass


class BananaA(Banana):
    pass


class BananaB(Banana):
    pass


class BananaC(Banana):
    pass


class Factory():
    def create_apple(self):
        pass

    def create_banana(self):
        pass


class FactoryA():
    def create_apple(self):
        return AppleA()

    def create_banana(self):
        return BananaA()


class FactoryB():
    def create_apple(self):
        return AppleB()

    def create_banana(self):
        return BananaB()


if __name__ == '__main__':
    factory = FactoryA()
    apple = factory.create_apple()
    print(apple)
# 外观模式，外观模式指的是，客户端在面对很多个对象时，如果都需要操控，就会特别复杂
# 在外观模式中，我们增加了一个外观类来进行对多个子系统的操控，并且客户端还需要调用这个外观类,是一个更高级的接口
# 例如建造模式，其实也有这个外观模式的意味，由建造者自己来控制组件的生成，而客户端只要去调用建造者就好了


class System1(object):
    def work(self):
        print("system 1 is work")


class System2(object):
    def work(self):
        print("system 2 is work")


class System3(object):
    def work(self):
        print("system 3 is work")


class System4(object):
    def work(self):
        print("system 4 is work")


class Operator(object):
    def __init__(self):
        self.sys = []

    def work(self):
        for sys in self.sys:
            sys.work()


class OperatorA(Operator):
    def __init__(self):
        super(OperatorA, self).__init__()
        self.sys.append(System1())
        self.sys.append(System2())


if __name__ == '__main__':
    operator = OperatorA()
    operator.work()
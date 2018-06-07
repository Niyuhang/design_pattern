# 桥接模式 主要在拥有多个产品，而每个产品又有多个具体实现方法
# 可以将产品的实现，和具体方法分开，进行桥接，这样子就可以减少类的设计，并且可以处理多维度的变化
# 利用多个类的组合来实现一组产品


class Pen(object):
    """抽象产品类"""
    def __init__(self, write_way):
        self.write_way = write_way()

    def write(self):
        self.write_way.write()


class YellowPen(Pen):
    def write(self):
        print("yellow")
        self.write_way.write()


class GreenPen(Pen):
    def write(self):
        print("green")
        self.write_way.write()


class Write(object):
    """抽象行为类"""
    def write(self):
        pass


class LeftWrite(Write):
    def write(self):
        print("写在左边")


class RightWrite(Write):
    def write(self):
        print("写在右边")


class Client():
    def write(self, pen, write_type):
        pen = pen(write_type)
        pen.write()


if __name__ == '__main__':
    client = Client()
    client.write(YellowPen, RightWrite)


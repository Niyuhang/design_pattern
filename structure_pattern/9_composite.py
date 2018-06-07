# 组织模式主要应对于多个局部和整体，让局部和整体都继承于同一个对象，
# 这样子就可以忽视整体和单个个体，统一进行处理，并且可以在整体里加入所有的个体，方便所有的递归
# 有两种组织模式，
# 一种是透明组织模式，在抽象基类定义所有方法，
# 第二种安全组织模式，只在整体类定义相应方法


class Component(object):
    """整个和个体的统一类"""
    def __init__(self, name):
        self.name = name

    def kill(self):
        pass


class Folder(Component):
    def __init__(self, name):
        self.files = []
        super(Folder, self).__init__(name)

    def add(self, obj):
        self.files.append(obj)

    def kill(self):
        print("对", self.name, "杀毒")
        for file in self.files:
            file.kill()


class ImageFile(Component):

    def kill(self):
        print("kill image", self.name)


class TextFile(Component):
    def kill(self):
        print("kill image", self.name)


if __name__ == '__main__':
    folder1 = Folder("文件夹1")
    folder2 = Folder("文件夹2")
    folder3 = Folder("文件夹3")

    file1 = ImageFile("你")
    file2 = ImageFile("我")
    file3 = TextFile("他")

    folder2.add(file1)
    folder2.add(file2)
    folder3.add(file3)

    folder1.add(folder2)
    folder1.add(folder3)

    folder1.kill()
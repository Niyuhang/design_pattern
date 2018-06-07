# 建造者模式主要运用于产品由多个组件构成时使用，有多个具体的建造者，这样子就可以进行各种产品的组建


class Build(object):
    def _create_hand(self):
        pass

    def _create_head(self):
        pass

    def get_man(self):
        self._create_hand()
        self._create_head()


class ChildrenBuild(Build):
    def _create_hand(self):
        print("child hand")

    def _create_head(self):
        print("child head")


class ManBuild(Build):
    def _create_hand(self):
        print("man hand")

    def _create_head(self):
        print("man head")


class Director(object):

    def get_man(self, build):
        build().get_man()


director = Director()
director.get_man(ChildrenBuild)
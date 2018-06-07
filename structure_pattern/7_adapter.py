# 适配器模式主要适配两个字，当我们有两个对象，而两个对象不兼容的时候，可以在此基础之上添加上一个适配器类
# 在适配器类里面封装一个接口，去调用不兼容对象的方法


class Adaptee(object):
    """需要进行修改的适配类"""
    def special_request(self):
        print("特殊的请求")


class Target(object):
    """最后的目标类"""
    def request(self):
        pass


class Adapter(Target):
    def request(self):
        adp = Adaptee()
        return adp.special_request()


# 利用适配器类就可以在不修改原有代码的基础上，进行适配

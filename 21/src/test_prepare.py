

class EntityMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        import collections
        print(mcs)
        print('__prepare__', name, bases)
        # 返回一个空的OrderedDict实例，类属性将存储在里面
        return collections.OrderedDict()

    def __init__(self, name, bases, attr):
        super().__init__(name, bases, attr)
        self.value = 878787


class A(metaclass=EntityMeta):
    pass

print(A.__dict__)


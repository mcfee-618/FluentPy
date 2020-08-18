
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    # 重载__getattrbute__方法对类实例的每个属性访问都有效
    # 访问属性时始终会调用__getattribute__() 方法。使用实例直接访问实例不存在的实例属性时,也会调用__getattribute__方法
    # def __getattribute__(self, item):
    #     print(item)
    #     return 222 #覆盖age

    # 在当前主流的Python版本中都可用
    # 如果通过常规属性查找未找到属性，返回属性self.name ，无法计算属性则引发AttributeError异常
    def __getattr__(self, item):
        return 55

    def __setattr__(self, key, value):
        print(key,value)
        print(self.__dict__)


    def __delattr__(self, item):
        print("del "+item)


a= Person("fei",18)
#print(a.age)
print(a.name11)
a.age=22
del a.age

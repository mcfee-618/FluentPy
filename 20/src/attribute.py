
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    # 访问属性时始终会调用__getattribute__() 方法。如果找到属性则返回之，否则调用__getattr__()方法。
    def __getattribute__(self, item):
        print(item)


    def __getattr__(self, item):
        return 55


a= Person("fei",18)
print(a.age)
print(a.name11)

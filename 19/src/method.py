import types
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    def eat(self):
        print("...%s正在吃。。"%self.name)
def run(self):
    print("...%s正在跑。。"%self.name)
Wang = Person("laowang",20)
Wang.eat()
Wang.run = types.MethodType(run,Wang) # MethodType可以把外部函数(方法)绑定到类或类的实例中
Wang.run()
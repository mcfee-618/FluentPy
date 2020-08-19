class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

laowang = Person("laowang",20)
print(laowang.name)
print(laowang.age)
laowang.addr = "北京"#动态添加的属性addr
print(laowang .addr)
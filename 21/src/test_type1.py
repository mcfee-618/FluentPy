
def init(self, name, value):
    self.name = name
    self.value = value


def show(self):
    print(self.name, self.value)


cls_attrs = dict()
cls_attrs['__init__'] = init
cls_attrs['show'] = show
cls = type("Person", (object,), cls_attrs)
print(cls)
obj = cls("2","3")
obj.name="jjj"
obj.show()


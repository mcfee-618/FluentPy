## 描述符

* 描述符是对多个属性运用相同存取逻辑的一种方式。描述符是实现了特定协议的类，这个协议包括 __get__ 、__set__ 和 __delete__ 方法。property类实现了完整的描述符协议。通常，可以只实现部分协议。

* 实现了 __get__ 、__set__ 或 __delete__ 方法的类是描述符。

* 对象属性的访问顺序:①.实例属性 ②.类属性 ③.父类属性 ④.__getattr__()方法
属性访问的默认行为是从一个对象的字典中获取、设置或删除属性。例如，a.x 的查找顺序会从 a.__dict__['x'] 开始，然后是 type(a).__dict__['x']，接下来依次查找 type(a) 的基类，不包括元类。如果找到的值是定义了某个描述器方法的对象，则 Python 可能会重载默认行为并转而发起调用描述器方法。

* 描述符的应用：描述器是一个强大而通用的协议。 它们是特征属性、方法静态方法、类方法和 super() 背后的实现机制。

## 描述符协议

* 如果一个对象定义了 __set__() 或 __delete__()，则它会被视为数据描述器。 仅定义了 __get__() 的描述器称为非数据描述器。

* 调用描述器：对于对象来说，机制是 object.__getattribute__() 中将 b.x 转换为 type(b).__dict__['x'].__get__(b, type(b)) 。这个实现通过一个优先级链完成，该优先级链赋予数据描述器优先于实例变量的优先级，实例变量优先于非数据描述器的优先级。对于类来说，机制是 type.__getattribute__() 中将 B.x 转换为 B.__dict__['x'].__get__(None, B) 。
* 要点：描述器由 __getattribute__() 方法调用，重写 __getattribute__() 会阻止描述器的自动调用，数据描述器始终会覆盖实例字典。非数据描述器会被实例字典覆盖。

* property的就是描述符实现的：调用 property() 是构建数据描述器的简洁方式，该数据描述器在访问属性时触发函数调用。它的签名是:
    property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
 ```
class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
 ```


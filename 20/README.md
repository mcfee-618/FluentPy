## 动态属性和特性

* 属性和特性：在Python中，数据的属性和处理数据的方法统称属性attribute。其实，方法只是可调用的属性。可以创建特性（property），在不改变类接口的前提下，使用存取方法 （即读值方法和设值方法）修改数据属性。

* 动态属性：Python 还提供了丰富的 API，用于控制属性的访问权限，以及实现动态属性。使用点号访问属性时（如 obj.attr ），Python 解释器会调用特殊的方法（如 __getattr__ 和 __setattr__ ）计算属性。用户自己定义的类可以通过 __getattr__ 方法实现“虚拟属性”，当访问不存在的属性时（如 obj.no_such_attribute ），即时计算属性的值。


* __getattr__和__getattribute__

    * __getattr__在当前主流的Python版本中都可用，重载__getattr__方法对类及其实例未定义的属性有效。也就属性是说，如果访问的属性存在，就不会调用__getattr__方法。这个属性的存在，包括类属性和实例属性。
    
    * __getattribute__仅在新式类中可用，重载__getattrbute__方法对类实例的每个属性访问都有效。访问实例不存在的实例属性时,也会调用__getattribute__方法,同时定义__getattribute__和__getattr__时，__getattr__方法不会再被调用，除非显示调用__getattr__方法或引发AttributeError异常。

* 备注：当在__getattribute__代码块中，再次执行属性的获取操作时，会再次触发__getattribute__方法的调用，代码将会陷入无限递归，直到Python递归深度限制（重载__setter__方法也会有这个问题）。

* 设置属性时始终会调用__setattr__() 方法，而删除属性时始终会调用__delattr__() 方法。 hasattr判定是否有这个属性,getattr用于获取属性。


## __init__ 和 __new__

__init__其实是初始化方法，真正的构造方法时__new__，我们几乎不需要自己编写 __new__ 方法，因为从 object 类继承的实现已经足够了。


## 特性

* property函数的作用是在新式类中返回属性值。内置的property经常用作装饰器，但它其实是一个类。在Python中，函数和类通常可以互换，因为二者都是可调用对象，而且没有实例化的new运算符，所以调用构造方法和调用工厂函数没有区别，只要能返回新的可调用对象，代替被装饰的函数，二者都可用作装饰器。


* property函数：property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

```
        get 是获取属性值的方法。
        fset 是设置属性值的方法。
        fdel 是删除属性值的方法。
        doc 是属性描述信息。如果省略，会把 fget 方法的 docstring 拿来用（如果有的话）
```
 
 
 备注：特性都是类属性，但是特性管理的其实是实例属性的存取，之前提到如果实例和所属的类有同名数据属性，那么实例属性会遮挡类属性。但是
 新添的类特性遮盖现有的实例属性。obj.attr 这样的表达式不会从 obj 开始寻找 attr ，而是从 obj.__class__ 开始，而且，仅当类中没有名为 attr 的特性时，Python 才会在 obj 实例中寻找。这条规则不仅适用于特性，还适用于整类描述符即覆盖型描述符。


* @property 语法糖提供了比 property() 函数更简洁直观的写法。

    被 @property 装饰的方法是获取属性值的方法，被装饰方法的名字会被用做 属性名。
    被 @属性名.setter 装饰的方法是设置属性值的方法。
    被 @属性名.deleter 装饰的方法是删除属性值的方法。


## 内置功能

* 特殊属性
```
__class__ :对象所属类的引用
__dict__  :一个映射，存储对象或类的可写属性,如果类有 __slots__ 属性，它的实例可能没有 __dict__ 属性。
__slots__ :类可以定义这个这属性，限制实例能有哪些属性。
```

* 特殊方法
```
dir([object]) ：列出对象的大多数属性。
getattr(object, name[, default])：从 object 对象中获取 name 字符串对应的属性。
hasattr(object, name) ： 如果 object 对象中存在指定的属性，或者能以某种方式（例如继承）通过 object 对象获取指定的属性，返回 True 。
setattr(object, name, value)：　把 object 对象指定属性的值设为 value ，前提是 object 对象能接受那个值。这个函数可能会创建一个新属性，或者覆盖现有的属性。
vars([object])：返回 object 对象的 __dict__ 属性；如果实例所属的类定义了 __slots__ 属性，实例没有 __dict__ 属性，那么 vars 函数不能处理那个实例
```

* 处理属性的特殊方法

使用点号或内置的 getattr 、hasattr 和 setattr 函数存取属性都会触发下述列表中相应的特殊方法。但是，直接通过实例的 __dict__ 属性读写属性不会触发这些特殊方法——如果需要，通常会使用这种方式跳过特殊方法。
```
obj.attr 和 getattr(obj, 'attr', 42) 都会触发 Class.__getattribute__(obj, 'attr') 方法。
把对象传给 dir 函数时调用，列出属性。例如，dir(obj) 触发 Class.__dir__(obj) 方法。
__getattr__(self, name) 仅当获取指定的属性失败，搜索过 obj 、Class 和超类之后调用。
__setattr__(self, name, value) 尝试设置指定的属性时总会调用这个方法。点号和 setattr 内置函数会触发这个方法。
```
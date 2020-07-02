## 把函数视作对象

* 在 Python 中，函数是一等对象.编程语言理论家把“一等对象”定义为满足下述条件的程序实体：
    * 在运行时创建
    * 能赋值给变量或数据结构中的元素
    * 能作为参数传给函数
    * 能作为函数的返回结果

* 高阶函数：接受函数为参数，或者把函数作为结果返回的函数是高阶函数，例如偏函数partial
* 匿名函数：lambda 关键字在 Python 表达式内创建匿名函数。然而，Python 简单的句法限制了 lambda 函数的定义体只能使用纯表达式。换句话说，lambda 函数的定义体中不能赋值，也不能使用 while 和 try 等 Python 语句。除了作为参数传给高阶函数之外，Python 很少使用匿名函数。

```
lambda 只是语法糖：与 def 语句一样，lambda 表达式会创建函数对象

```

* 可调用对象：除了用户定义的函数，调用运算符（即 () ）还可以应用到其他对象上。如果想判断对象能否调用，可以使用内置的 callable() 函数。
    * 用户定义的函数：使用 def 语句或 lambda 表达式创建。
    * 内置函数：使用 C 语言（CPython）实现的函数，如 len 或 time.strftime 。
    * 内置方法：使用 C 语言实现的方法，如 dict.get 。
    * 方法：在类的定义体中定义的函数。
    * 类：调用类时会运行类的 __new__ 方法创建一个实例，然后运行 __init__ 方法，初始化实例，最后把实例返回给调用方。因为 Python 没有 new 运算符，所以调用类相当于调用函数。（通常，调用类会创建那个类的实例，不过覆盖 __new__ 方法的话，也可能出现其他行为。）
    * 类的实例：如果类定义了 __call__ 方法，那么它的实例可以作为函数调用。
    * 生成器函数：使用 yield 关键字的函数或方法。调用生成器函数返回的是生成器对象。

* 函数自省【对象本身属性】：除了 __doc__ ，函数对象还有很多属性。使用 dir 函数可以探知相关的属性。函数对象有个 __defaults__ 属性，它的值是一个元组，里面保存着定位参数和关键字参数的默认值。仅限关键字参数的默认值在 __kwdefaults__ 属性中。然而，参数的名称在 __code__ 属性中，它的值是一个 code 对象引用，自身也有很多属性。    

## code对象与函数对象

Code对象表示字节编译的可执行Python代码或字节码。Code对象和函数对象之间的区别在于：

* 函数对象包含对函数的全局变量（定义它的模块）的显式引用，而Code对象不包含上下文
* 默认参数值也存储在函数对象中，而不是存储在Code对象中（因为它们表示在运行时计算的值）。
* 与函数对象不同，代码对象是不可变的【函数对象可以增加属性】，并且不包含（直接或间接）可变对象的引用。

## partial函数实现

functools.partial 这个高阶函数用于部分应用一个函数。部分应用是指基于一个函数创建一个新的可调用对象，把原函数的某些参数固定，从而简化函数的使用，这个函数的底层实现是闭包【一个函数嵌套一个函数，内层函数作为返回值】。

```
def partial(func, *args, **keywords):
    """New function with partial application of the given arguments
    and keywords.
    """
    if hasattr(func, 'func'):
        args = func.args + args
        tmpkw = func.keywords.copy()
        tmpkw.update(keywords)
        keywords = tmpkw
        del tmpkw
        func = func.func

    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords) # 添加到指定字典dict里的字典
        return func(*(args + fargs), **newkeywords) #装包
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

## 装包与拆包
* 装包就是把未命名的参数放到元组中，把命名参数放到字典中
* 拆包将一个结构中的数据拆分为多个单独变量中 *args **kwargs
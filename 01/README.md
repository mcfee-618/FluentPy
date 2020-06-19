##特殊方法

1. 特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它们。也就是说没有 my_object.__len__() 这种写法，而应该使用 len(my_object) 。在执行 len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 Python 会自己去调用其中由你实现的 __len__ 方法。
2. 如果是 Python 内置的类型，比如列表（list ）、字符串（str ）、字节序列（bytearray ）等，那么 CPython 会抄个近路，__len__ 实际上会直接返回 PyVarObject 里的 ob_size 属性，PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。直接读取这个值比调用一个方法要快很多。

## 神奇的语法糖

很多时候，特殊方法的调用是隐式的，比如 for i in x: 这个语句，背后其实用的是 iter(x) ，而这个函数的背后则是 x.__iter__() 方法。当然前提是这个方法在 x 中被实现了。

## 注意事项

通常你的代码无需直接使用特殊方法。除非有大量的元编程存在，直接调用特殊方法的频率应该远远低于你去实现它们的次数。唯一的例外可能是 __init__ 方法，你的代码里可能经常会用到它，目的是在你自己的子类的 __init__ 方法中调用超类的构造器。

## 特殊方法

https://docs.python.org/zh-cn/3/reference/datamodel.html
https://ltoddy.github.io/essay/2018/05/27/python-magic-methods.html

## len为什么不是普通方法

len之所以不是一个普通方法，是为了让 Python 自带的数据结构可以走后门，abs 也是同理。但是多亏了它是特殊方法，我们也可以把 len 用于自定义数据类型。

## repr和str区别

__repr__ 和 __str__ 来满足这个要求。前者方便我们调试和记录日志，后者则是给终端用户看的

## 延伸阅读

https://docs.python.org/3/reference/datamodel.html 
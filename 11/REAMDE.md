## 从鸭子类型到抽象基类

从鸭子类型的代表特征动态协议，到使接口更明确、能验证实现是否符合规定的抽象基类（Abstract Base Class，ABC）。

* Python文化中的接口和协议：Python语言没有 interface 关键字，而且除了抽象基类，每个类都有接口：类实现或继承的公开属性（方法或数据属性），包括特殊方法，如__getitem__ 或 __add__。协议是接口，但不是正式的（只由文档和约定定义），因此协议不能像正式接口那样施加限制（后面会说明抽象基类对接口一致性的强制）。一个类可能只实现部分接口，这是允许的。

* 猴子补丁：在运行时修改类或模块，而不改动源码

    ``` 
    def set_card(deck, position, card):
        deck._cards[position] = card
    猴子补丁，把自定义的函数赋值给__setitem__，把它变成可变的。
    FrenchDeck.__setitem__ = set_card
    ``` 

def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        ...
    field_names = tuple(field_names)

    # 定义初始化函数
    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    # 定义成可迭代对象
    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    # 定义输出
    def __repr__(self):
        # 输出values，其中的zip参数里面的self会调用__iter__
        values = ', '.join('{}={!r}'.format(*i)
                           for i in zip(self.__slots, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(
        __slots__=field_names,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__
    )

    return type(cls_name, (object,), cls_attrs)


if __name__ == '__main__':
    Dog = record_factory('Dog', 'name weight owner')
    print(type(Dog))  # <class 'type'>

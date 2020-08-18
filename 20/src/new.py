class Foo(object):
    def __init__(self, bar):
        self.bar = bar
 
 
def object_maker(the_class, some_arg):
    new_object = the_class.__new__(the_class)
    if isinstance(new_object, the_class):
        the_class.__init__(new_object, some_arg)
    return new_object
 
 
demo1 = Foo("bar1")
demo2 = object_maker(Foo, "bar2")
print(demo1)
print(demo1.bar)
print(demo2)
print(demo2.bar)
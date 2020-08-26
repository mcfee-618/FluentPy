
class MyMetaClass(type):

    def __init__(self,name,bases,attr):
        super().__init__(name,bases,attr)  
        print(name,bases,attr)
        self.show = "222" 

    # def __new__(cls,*args):
    #     print("new")
    #     return type(args)



class A(metaclass = MyMetaClass):
    
    name=333
    
    pass

print(type(A))
print(A.__dict__)



    

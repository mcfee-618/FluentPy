# coding=utf8

class A:

    def __init__(self):
        self.x=3

    def __len__(self):
        """
          python内置的特殊方法
        :return:
        """
        return 3

    def __getattribute__(self, item):
        print(item)
        return 6


class Complex:

    def __init__(self,num):
        self.num =num

    def __mul__(self, other):
        return (self.num+1)*(other.num+1)


a= Complex(2)
b= Complex(3)
print(a*b)

obj= A()
print(obj.x)
print(obj.y) #使用实例直接访问实例不存在的实例属性时,也会调用__getattribute__方法
c=list()
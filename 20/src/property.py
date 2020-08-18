
class Student:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        print('获取属性时执行的代码')
        return self._age

    @age.setter
    def age(self, age):
        print('设置属性时执行的代码')
        self._age = age

    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age


student = Student()

# 设置属性
student.age = 18
"""
设置属性时执行的代码
"""

# 获取属性
print('学生年龄为：' + str(student.age))
"""
获取属性时执行的代码
学生年龄为：18
"""

# 删除属性
del student.age
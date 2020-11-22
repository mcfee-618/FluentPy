import inspect

dd=2

def add(x,y):
    print(dd)
    current_frame = inspect.currentframe()
    print(current_frame)
    print("局部变量")
    print(current_frame.f_locals)
    print("全局变量")
    print(current_frame.f_globals)
    print("上一个栈帧")
    print(current_frame.f_back)
    
    z = x+y
    return z


def main():
    add(2,3)
main()
    
import dis

a=33

def test1():
    print(a)

def test2():
    print(a)
    a=a+1
    print(a)


def test3():
    global a
    a+=1

dis.dis(test3)
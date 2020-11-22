import dis


def add(x,y):
    z = x+y
    return z

def sum(nums):
    count = 0
    for num in nums:
        count+= num
    return count

def div(a,b):
    return a/b

def sum_while(nums):
    count=0
    i=0
    while(i<len(nums)):
        count += nums[i]
        i+=1
    return count

def test():
    a=22
    def test1():
        nonlocal a
        a+=1
        print(a)
    return test1
        



def main():
    bytecodes = dis.dis(test())
    b=test()
    b()
    b()
    print(b.__code__.co_freevars)
    #dis.dis(div)
    div("2",-999)

main()
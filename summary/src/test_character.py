# coding:utf-8
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


def readlines(path):
    with open(path, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            #line=line.decode("utf-8")
            yield line


value = '好'

lines = readlines("input/a.txt")
for line in lines:
    print(type(line))
    if value == line:
        print(value.encode("utf-8"))
        break

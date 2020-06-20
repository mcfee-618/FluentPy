

a=[2,3,4]
b=[5,6,7,8]

#### 列表生成式
print([x for x in a])
print([x for x in a if x>3])
print([(x,y) for x in a
         for y in b])

#### 生成器生成式
d=  (x for x in a)
print(d) # <generator object <genexpr> at 0x1045a50a0>
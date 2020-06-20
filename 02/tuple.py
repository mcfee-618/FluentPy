import collections

info=("feipeixuan",27,"牛逼")

### 元组拆包
name,age,_ = info
print(name,age)

name,*others =info
print(others) #[27, '牛逼']

### 嵌套元组拆包
info = (222,(3,5))
c,(x,y) =info
print(x,y)

### 命名元祖
Card = collections.namedtuple('Card', ['rank', 'suit']) #
print(Card(2,3))
Person = collections.namedtuple('Person',['name','jjj'])
print(Person("fei",(22,33)))
# Card(rank=2, suit=3)
# Person(name='fei', jjj=(22, 33))
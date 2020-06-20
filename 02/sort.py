

a=[2,3,4,5,6,78]
b=['22','333','444','888888']
a.sort(reverse=True) #[78, 6, 5, 4, 3, 2]
b.sort(key=len)
print(b)

c={"aaa":22222,"bb":3}
print(sorted(c.items(),key=lambda item:item[1])) # 按照value 排序
print(c.items())


s = 'bicycle'
s[::3] #'bye'
s[::-1] #'elcycib'
print(s[::-2]) # eccb'
print(id(s[::-2]))
print(id(s[::-1]))  #id相同
print(type((s[::-2])))

list = [3,4,5,6,7,8]
a=list[::-1]
b=list[1:3]
print(id(a),id(b)) #id不同

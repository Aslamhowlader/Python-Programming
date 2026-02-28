'''d={x: x**2 for x in range(5)}
print(d)

key=["a","b","c"]
value=[1,2,3]
d={k:v for k,v in zip(key,value)}
print(d)

even={x:x**2 for x in range(10) if x%2==0 }
print(even)

city={"dhaka":34,"Briashal":45,"Buphal":56}
s={key :value for (key ,value) in city.items()}
print(s)


city={"dhaka":34,"Briashal":45,"Buphal":56}
d={key: value for (key,value) in city.items() if value==45}
print(d)

S={x:x**2 for x in range(10) if x%2==0}
print(S)
'''
#Set Comprehension
w=["Aslam","Salamk","Kama"]
l={len(x) for x in w}
print(l)
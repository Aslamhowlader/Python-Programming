
frist={1,2,3,4,5,6,7}
secoun={4,6,7,8,9,4,3}
print(frist | secoun )
print(frist & secoun)
print(frist - secoun)


number={1,2,3,4,5,6}
empty=set()
print(number)
print(empty)

num={2,3,4,6,7,3,4}
print(num)

my_list=[2,4,6,2]
print(list(set(my_list)))


a={2,4,6,7}
b={4,5,2,3}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a<=b)
print(a>=b)


from os import remove

s={2,5,4,3}
s.add(1)
print(s)
s.remove(4)
print(s)
s.pop()
print(s)
s.clear()
print(s)











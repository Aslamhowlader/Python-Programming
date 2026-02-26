'''
num=[1 ,2,3,4,5]
n=[x*x for x in num]
print(n)

num=[1,2,3,4,5,6,8]
n=list(filter(lambda x: x%2==0,num))
print(n)
'''
num=[1,2,3,4,5,6,8]
r=[x for x in num if x%2==0]
print(r)
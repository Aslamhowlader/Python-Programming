
num=[1 ,2,3,4,5]
n=[x*x for x in num]
print(n)

num=[1,2,3,4,5,6,8]
n=list(filter(lambda x: x%2==0,num))
print(n)

num=[1,2,3,4,5,6,8]
r=[x for x in num if x%2==0]
print(r)

number=[1,3,4,5,6,7,8]
n=[i**2 for i in number]
print(n)

s=[]
for i in range(10):
    s.append(i**2)
print(s)

even=[x for x in range(20) if x%2==0]
print(even)

result=["even" if i%2==0 else "odd" for i in range(5)]
print(result)

matrix=[[j for j in range(5)] for i in range(5)]
print(matrix)

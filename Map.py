
celsius_temp=[10.2,39,48,56]
fahrenheit_temp=list(map(lambda temp: (temp* 9/5)+32,celsius_temp))
print(fahrenheit_temp)

a=[2,3,4]
b=[4,5,6]
c=list(map(lambda x,y: x+y, a,b))
print(c)


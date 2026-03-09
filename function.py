'''
def fun(v1,v2,v3):
   return v1,v2,v3
n1,n2,n3=fun(2,3,4)
print(n1,n2,n3)


def fun1(v1):
    print(f"Hello,{v1}")
fun1("ASlam")


def fun2(a,b):
    return a+b, a-b, a*b, a/b, a**b, a//b

n1,n2,n3,n4,n5,n6 = fun2(6,8)

print("Addition:", n1)
print("Subtraction:", n2)
print("Multiplication:", n3)
print("Division:", n4)
print("Power:", n5)
print("Floor:", n6)

def fun3(age):
    if age > 18:
        return "Adult"
    elif age < 18:
        return "Child"
    else:
        return "Minor"

print("Age:", fun3(int(input("Enter the input: "))))

def greet(name, massage="Good morning"):
    print(f"{name},{massage}")
greet("Aslam")
greet("Salam","Good night")


def info(name,age,city):
    print(f"{name},{age},{city}")
info(age=23,city="Dhaka",name="Aslam")
def total(*num):
    return sum(num)
sum1=total(2,3,4)
sum2=total(5,7,8,9,3)
print(sum1)
print(sum2)


def gret(*names):
    for name in names:
        print(f"Hello,{name}")
gret("Aslam","Salam","Kamal")

def info(**info):
    for key,value in info.items():
        print(f"{key} {value}")

info(name="Aslam",age=25,city="Dhaka")




def func(a,b,*n,**k):
    print(f"a={a}")
    print(f"b={b}")
    print(f"n={n}")
    print(f"k={k}")

func(1,2,3,4,5,6, x=34,y=67)


def seuare(x):
    return x**2
print(seuare(3))



a=lambda x:x**2
print(a(3))


add=lambda a ,b:a+b
print(add(3,5))


is_even=lambda x: x%2==0
print(is_even(23))


student=[("ASlam",85),("Kamal",45),("Jamal",34)]
student.sort(key=lambda x:x[1])
print(student)

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)



my_list = [1,2,3,4,5,6,7,8]
add_1 = lambda x: x**2

result = list(map(add_1, my_list))
print(result)



student=[("Aslam",85),("Slam",34),("Kamal",56)]
print(student.sort(key=lambda x:x[1]))



def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5

    inner()
    print(x)


outer()

'''











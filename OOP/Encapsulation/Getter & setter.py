class student:

    def setter(self,name):
        self.__name=name
    def getter(self):
        return self.__name
    def setter1(self,age):
        self.__age=age
    def getter1(self):
        return self.__age
ob=student()
ob.setter("ASlam")
n=ob.getter()
print(n)
ob.setter1(12)
a=ob.getter1()
print(a)
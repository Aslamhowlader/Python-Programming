class Aslam:
    School="BUBT"
    def __init__(self,name,age ):
         self.name=name
         self.age=age
    def display(self): #instance method
        print(self.name,self.age)

    @classmethod
    def show(cls,new_School):
        cls.School=new_School
    @staticmethod
    def add(a,b,c):
        return a+b+c
ob=Aslam("Salam",23)
ob.display()
Aslam.show("Kanak dia SS high School")
print(Aslam.School)
g=Aslam.add(2,4,5)

print(g)




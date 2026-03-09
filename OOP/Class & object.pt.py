class studnt:
    school="Kanak dia SS school and collage"
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"I am {self.name } , age {self.age}")
    def study(self,subject):
        print(f"{self.name}  is studing {subject}")

studnt1=studnt("ASlam",23)
studnt2=studnt("Slam",45)
print(studnt1.name)
print(studnt1.age)
studnt1.introduce()
studnt1.study("python")

studnt2.introduce()
studnt2.study("python2")





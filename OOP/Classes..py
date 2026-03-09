class student:
    School="python High School"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __index__(self):
        self.name="Aslsm"
        self.age=20
    def display(self):
        print("Age :",self.age)
        print("name: ",self.name)
    def introduce(self):
        print(f"I am {self.name}, age {self.age}")

    def study(self, subject):
        print(f"{self.name} is studying {subject}")
ob1=student("Aslam",23)

ob1.display()
ob1.introduce()
ob1.study("C++")


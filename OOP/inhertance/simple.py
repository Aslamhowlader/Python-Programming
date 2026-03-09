class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def dis(self):
        print(self.name)
        print(self.id)
class CSE(student):
     def __init__(self,name,id,intake,section):
         super().__init__(name,id)
         self.section=section
         self.intake=intake
     def dis1(self):
         print(self.section)
         print(self.intake)
ob=CSE("Aslam",12,53,1)
ob.dis()
ob.dis1()

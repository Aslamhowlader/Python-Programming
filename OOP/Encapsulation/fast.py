class student:
    def __init__(self,name,age,id):
        self.name=name
        self._age=age
        self.__id=id
    def __privatedisplay(self):
        print(self.name)
        print(self._age)
        print(self.__id)
    def display(self):
        self.__privatedisplay()
class datile(student):
    def __init__(self,father_name,mother_nname,NID,name,age,id):
        super().__init__(name,age,id)
        self._father_name=father_name
        self._mother_name=mother_nname
        self.__NID=NID
    def __privatedisplay1(self):
        print(self._father_name)
        print(self._mother_name)
        print(self.__NID)
    def display1(self):
        self.__privatedisplay1()

ob=datile("Slam","Rabaya",2738943978,"Aslam",12,27)
ob.display()
ob.display1()
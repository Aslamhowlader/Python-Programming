from tkinter.font import names


class Aslam:
    def __init__(self,name,id):
      self.name=name #instance variable
      self.id=id

    def display(self):

        print(self.name,self.id)

object=Aslam("Aslam",12)
object.display()
object1=Aslam("Salam",13)
object1.display()



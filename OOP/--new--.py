'''class student:
    def __new__(cls):
        print("Super mathod")
        return  super().__new__(cls)
    def __init__(self):
        print("Defalt conster")
ob=student()
'''
class singleton:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            print("Creating new instance")
        else:
            print("Using existing instance")
        return cls._instance
    def __init__(self):
        print("Initiating instance")
ob=singleton()
ob1=singleton()
print(ob is ob1)
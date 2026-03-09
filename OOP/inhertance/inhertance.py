class student:
    def __init__(self):
        print("student Class")
class CSE(student):
    def __init__(self):
        super().__init__()
        print("CSE CLASS")
class BBA(CSE):
    def __init__(self):
        super().__init__()
        print("BBA Class")
ob=BBA()
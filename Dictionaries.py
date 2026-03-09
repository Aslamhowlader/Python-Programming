'''d={
    'name':"Aslm",
    "age":23,
    "city":"Dhaka"
   }

d.update({'name':"Salam"})
d.update({"age":34})
d.pop("age")
d.clear()
for key ,value in d.items():
    print(key,":",value)


student={"Name":"Aslam","Age":23}
del student["Name"]
print(student)
student.pop("Age")
print(student)
'''
student={"Name":"Aslam","Age":23}

print(student.keys())
print(student.values())
print(student.items())
print("Name" in student)



















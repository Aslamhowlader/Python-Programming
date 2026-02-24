"""age=int(input("Enter the number: "))
if age>18:
    print("Adult peroson")
else:
    print("childe")

mark=int(input("Enter the mark:"))
if mark>=80:
    print("A+")
elif mark>=75:
    print("A")
elif mark >= 70:
    print("A-")
elif mark >=65:
    print("B+")
elif mark>=60:
    print("B")
elif mark>=55:
    print("B-")
elif mark>=50:
    print("C+")
elif mark>=45:
    print("C")
elif mark>=40:
    print("C-")
elif mark>=40:
    print("D")
else:
    print("fail")


age=int(input("Enter the number: "))
has_licence=True
if age>=18:
    if has_licence:
        print("you can drive")
    else:
        print("you need a license")
else:
    has_licence=False
    if has_licence:
        print("has lince is falase")
    else:
        print("has lince is not falase")


age=int(input("Enter the number: "))
has_ticket=True
if age>=18 and has_ticket:
    print("you can enter")

if age<12 or age<65:
    print("your get a discount")
if not has_ticket:
    print("wellcame")


for i in range(5):
    print(i)

for i in range(1,20):
    print(i , end=" ")

for i in range(0,20,2):
    print(i,end=" ")

F=["apple","banana","mango","gro","cow"]
for i in F:
    print(i,end=", ")
"""
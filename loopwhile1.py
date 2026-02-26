'''count=0
while count <=10:
    print(count)
    count+=1
    if count==7:
        break

print("out loop")

list_my=["1","2","3"]
list1_my=["4","2","5"]
#break
for i in list_my:
     for j in list1_my:
          print(i ,":",j)
          if i==j:
              break
     print("out from inner loop")
print("out from outer loop")

#continue
for i in range(3):
     for j in range(3):
        print(i,":",j)
        if i==j:
          continue
        print("HI")
print("outer loop")

for i in range(5):
   pass

i=0
while i<=10:
    if i==4:
      i+=1
      continue
    print(i)
    i+=1

i=0
while i<=10:
    if i==5:
        pass
    print(i)
    i+=1



for i in range(5):
    if i == 2:
        pass
    print(i)


for i in range(5):
    print(i)
else:
    print("Loop completed normally!")

'''
n= [2, 5,7, 9, 11]
for i in n:
    if i == 7:
        print("found")
        break
else:
    print("Not found")
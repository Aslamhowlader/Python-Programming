n=[23,4,6,7,8]
for j in n:
    for i in range(2,j):
       if j%i==0:
         print("Not prime")
         break
    else:
         print("prime")
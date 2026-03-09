import pandas as pd
data=[100,200,300,500,"Aslam",]
series=pd.Series(data,index=['a','b','c','d','e'])
print(series.loc['e'])

s=pd.Series([1,2,3,4,5])
print(s)

#from disctionary
data={"apple":100,'banana':300,'Chearry':150}
s=pd.Series(data)
print(s)
print(s.values)
print(s.index)
print(s.dtype)
print(s.describe())

import pandas as pd

data = [100, 200, 300, 500]
s = pd.Series(data, index=['a','b','c','d'])

print(s[s >= 200])


#Datafeame
data={
    "Name":["Aslam","Kalam","jamal"],
    "Age":[30,40,38]
}
df=pd.DataFrame(data)
print(df)













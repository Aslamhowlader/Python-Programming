import pandas as pd

data={
    'Name':['Aslam','karim','jamil','Rahim'],
    'Age':[24,49,56,67]

}

df=pd.DataFrame (data,index=["Employee1","Employee2","employee3","Employee4"])
#adding new columns
df["Job"]=["Cook","N/A","Cashier","Banana"]
df["Roll"]=["A","B","C","D"]
#adding new row
new_row=pd.DataFrame([
                      {"Name":"Jewel","Age":28,"Job":"Engnering","Roll":"f"},
                      {"Name":"gaha","Age":27,"Job":"Engne","Roll":"y"},
                      {"Name":"Jdhf","Age":28,"Job":"En","Roll":"x"}

                      ],index=["Emplayee5","Emplayee6","Emplayee7"])
df=pd.concat([df,new_row])
print(df)

import pandas as pd

data = {
    'Student': ["Aslam","Salam","Jamal","Kamal"],
    'rank': [1,2,3,4,5],
    'marks': [97,95,64,37,94]
}


min_len = min(len(lst) for lst in data.values())


for key in data:
    data[key] = data[key][:min_len]

df = pd.DataFrame(data)
print("Student Records\n")
print(df)
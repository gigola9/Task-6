import pandas as pd

df = pd.read_excel("staff_1000.xlsx")
headers = []
for col in df.columns:
    headers.append(col)

newArr = []

for x in df.index:
    if 30 < df.loc[x, "Age"] < 40:
        newArr.append(df.loc[x].values)

df1 = pd.DataFrame(newArr)

df1.to_excel("staff_age.xls", index=False, header=headers)

import pandas as pd

df = pd.read_excel("data.xlsx")
print(df)
vl = df.values
res = []

for x in vl:
  if x[0].count('a') > 0:
    res.append(x)

df1 = pd.DataFrame(res)

df1.to_excel("datanew.xlsx", sheet_name='sheet3', index=False, header=False)

import pandas as pd

df = pd.read_excel("data.xlsx")
print(df)
df.to_excel("datanew.xlsx", index=False, header=False)

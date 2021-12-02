import pandas as pd

df = pd.read_excel("data.xlsx")
mx = max(df[["random3"]].values)


for x in df.index:
  if df.loc[x, "random3"] == mx:
    df.loc[x].to_excel("datanew.xlsx", sheet_name='sheet4')

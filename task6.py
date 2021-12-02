import pandas as pd

df = pd.read_excel("file_example_XLSX_1000.xlsx")

print(df.sort_values('Id'))

print(f'average: {df["Age"].mean()}')
print(f'median: {df["Age"].median()}')
print(f'mode: {df["Age"].mode()}')

mx = max(df[["Age"]].values)
mn = min(df[["Age"]].values)

print('ყველაზე მაღალი ასაკის მომხმარებლები')
for x in df.index:
    if df.loc[x, "Age"] == mx:
        print(df.loc[x].values)

print('ყველაზე დაბალი ასაკის მომხმარებლები')
for x in df.index:
    if df.loc[x, "Age"] == mn:
        print(df.loc[x].values)

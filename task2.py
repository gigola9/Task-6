import pandas as pd
import random

data = []
names = ['gio', 'mari', 'dato', 'ani', 'jack']
surname = ['asanidze', 'green', 'dvali', 'brown']
dic = {}
for i in range(0, 100):
    rn1 = random.randint(1, 100)
    nm = names[random.randint(0, 3)]
    sr = surname[random.randint(0, 3)]
    rn2 = random.randint(2000, 5000)

    data.append({
        'random1': rn1,
        'name': nm,
        'surname': sr,
        'random2': rn2
    })

df = pd.DataFrame(data)
print(df)
df.to_excel("data.xlsx", sheet_name='sheetTwo', index=False, header=False)

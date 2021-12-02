import pandas as pd
import random

data = []
dic = {}
while len(dic) != 100:
    st = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(0, 10))
    rn1 = random.randint(0, 10)
    rn2 = random.randint(1, 7)
    rn3 = random.randint(1, 101)

    if not (rn3 in dic):
        dic[rn3] = rn3
        data.append({
            'string': st,
            'random1': rn1,
            'random2': rn2,
            'random3': rn3
        })

df = pd.DataFrame(data)
print(df)
hd = ['string', 'random1', 'random2', 'random3']
df.to_excel("data.xlsx", sheet_name='sheetOne', index=False, header=hd)

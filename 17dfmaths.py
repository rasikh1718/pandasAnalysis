import pandas
dic={
    'london':[15,19,17],
    'mumbai':[39,36,37],
    'dubai':[43,47,45],
    'berlin':[12,15,13]
}
df=pandas.DataFrame(dic)
print(dic)
df=df.add(5)
# print(df)
df=df.sub(1.5)
#print(df)
df=df.mul(2)
#print(df)
df=df.div(2)
print(df)
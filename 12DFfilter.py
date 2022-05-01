import pandas
url='http://sohamspring.azurewebsites.net/api/players'

df=pandas.read_json(url)
# print(df)

# df1=df[df['country']=='england']
df1=df[df['country']!='spain']
print(df1)

df1=df[df['age']>25]
print(df1)

df1=df[(df['country']=='england') & (df['position']=='forward')]
print(df1)

df1=df[(df['club']=='Liverpool') | (df['country']=='France')]
print(df1)

pno=[133,141,145,139,163]
df1=df[df['playerno'].isin(pno)]
print(df1)
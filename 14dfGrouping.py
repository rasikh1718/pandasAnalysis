import pandas
url='http://sohamspring.azurewebsites.net/api/players'
df=pandas.read_json(url)
#print(df)

df1=df.groupby('club')
# print(df1)


for rec in df1:
    print(rec)

print(df.groupby('country').groups)
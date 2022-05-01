import pandas

df=pandas.read_csv('orders.csv')
print(df)
print('-'*50)

print('status of NULL values in DF')
print(pandas.isnull(df))
print('-'*50)


print('remove rows with null values')
df1=df.dropna()
print(df1)
print('-'*50)

print('remove columns with null values')
df1=df.dropna(axis=1)
print(df1)
print('-'*50)

print('rename null values')
df['userid'].fillna('NoUserID',inplace=True)
print(df)
print('-'*50)

print('replace values')
df2=df.replace('trial','discard')
print(df2)

 
import pandas

url='http://sohamspring.azurewebsites.net/api/players'
df=pandas.read_json(url)
print(df)


print('selecting data from single column')
print(df['playernm'])

print('selecting data from multiple column')
print(df[['playernm','country']])
print('selecting data row,using index')
print(df.loc[14])
print(df.loc[9,'playernm'])
print(df.loc[9,['playernm','age']])
print(df.loc[10:,['country','club']])
print(df.loc[15:])
print(df.loc[2:8,'playernm'])
print(df.loc[:5])
import pandas
url='http://sohamspring.azurewebsites.net/api/players'
df=pandas.read_json(url)
print(df)
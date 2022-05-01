import pandas
import ssl

url='https://restapi.sohamglobal.in/api/accounts'
# ssl._create_default_https_context=ssl._create_unverified_context
ssl._create_default_https_context=ssl._create_unverified_context
df=pandas.read_json(url)
print(df)

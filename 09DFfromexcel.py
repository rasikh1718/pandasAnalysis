# import pip install openpyxl
import pandas
file=pandas.ExcelFile('companies.xlsx')
df=file.parse('sheet1')
print(df)


#df.to_csv("comp.csv")




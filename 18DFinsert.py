import pandas
dic={
    'name':['praffull','soham','sharayu','megha'],
    'tech':['java','cloud','spark','asp.net']
}

df=pandas.DataFrame(dic)
print(df)

df.insert(1,'code',9)
df.loc[1,'code']='rasikh'
print(df)
df.insert(3,'company','sohamglobal')
print(df)

df.loc[2,'code']=13
df.loc[1,'company']='accenture'
print(df)
# print(df)
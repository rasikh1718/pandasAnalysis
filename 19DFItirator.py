import imp


import pandas

dic={
    'name':['praffull','soham','sharayu','megha'],
    'tech':['java','cloud','spark','asp.net'],
    'location':['london','dubai','mumbai','kolkata'],
    'salary':[23500.00,74600.00,81300.00,47500.00]
}
df=pandas.DataFrame(dic)
print(df)
sum=0.0
for i,j in df.iterrows():
    print('i=',i)
    print(j)
    print(j['name'].upper())
    sum+=j['salary']
    print('-'*35)
print('total salary of all employees',sum)
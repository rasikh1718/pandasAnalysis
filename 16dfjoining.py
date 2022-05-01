import pandas
custdf=pandas.read_csv("customers.csv")
orddf=pandas.read_csv("orders.csv")

print('Inner join - only matching data from both DF')
dfinner=custdf.merge(orddf,on='userid',how='inner')
print(dfinner)
print('--'*30)

print('Left outer join- all customers with matching orders or NaN')
dfleft=custdf.merge(orddf,on='userid',how='left')
print(dfleft)


print('Right outer join- all orders with matching customers or NaN')
dfright=custdf.merge(orddf,on='userid',how='right')
print(dfright)
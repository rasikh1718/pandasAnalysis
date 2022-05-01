import pandas

dic={
    'filmnm':['sholay','pk','swades'],
    'releaseyr':[1975,2014,2004],
    'actor':['amitabh bachchan','amir khan','shah rukh khan'],
    'music':['r d burman','shantanu moitra','a r rahman'],
    'imdbrating':[8.1,8.2,8.0],
    'grossmn':[350,865,295]
}
df=pandas.DataFrame.from_dict(dic)
print(df)
print('--'*30)
df1=df.sort_values('grossmn')
print(df1)

df1=df.sort_values('actor',ascending=False)
print(df1)

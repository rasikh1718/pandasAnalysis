import numpy
import pandas

dict1={
    # key : values
    'name':['rasikh','altamsh','huzefa','bilal'],
    'rollno':[101,102,103,104],
    'subject':['physics','math','biology','arts']

}

pd=pandas.DataFrame(dict1)
print(pd)



pd=pandas.DataFrame.from_dict(dict1)
print(pd)

#  to convert the csv
pd.to_csv('class.csv')
# to remove the indices
pd.to_csv('freind_indixes_false.csv',index=False)
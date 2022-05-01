import numpy
import pandas

arr=numpy.array(
    [
        ['rasikh','altamsh','bilal','gulam'],
        ['realme','oppo','samsung','apple'],
        ['opratoe','dataanalysis','programmer','devoloper'],
        [250000,65000,6500,8562],
        ['python','.net','java','cloude']
    ]
 
)
# df=pandas.DataFrame(arr)
# print(df)


row=['empnm','compsny','dob','tool','row']
col=['name','com','disg','salary']
df=pandas.DataFrame(arr,row,col)
print(df)
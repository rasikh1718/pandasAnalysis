import numpy
import pandas

lst=['volkswegon','bmw','skoda','hyundai','tyota','audi','ford']
arr=numpy.array(lst)

print('creating pandas searies from numpy array')
ser=pandas.Series(arr)
print(ser)
# retrive element from series
print(ser[2])

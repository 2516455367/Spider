import os
import pandas as pd
a=['1','20','3']
b=['c','d','f']
# df=pd.DataFrame({'职位名': a, '公司名': b})
# print(df)
# path=os.getcwd()
# print(path)
# df.to_excel('{}./1.xlsx'.format(path),index=False)
def ttt(x):
    for i in x:
        yield i
a=ttt([1,2,3,4,5,6])
for i in a:
    print(i)
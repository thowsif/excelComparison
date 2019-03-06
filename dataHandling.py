import pandas as pd 
import numpy as np 
import xlrd
import xlsxwriter


sheet1 = pd.read_excel("sheet1.xls")
#print(template1['Genres'])
#data = pd.DataFrame(template1)
sheet2 = pd.read_excel("sheet2.xls")
#df = data['Genres']
#print(df)
# print(data['Language'])
# i=0
# for s1 in sheet1:
#     for s2 in sheet2:
#         if s1['Title'] == s2['Title']:
#             if s2['Actor 1'] == nan:
#                 s2['Actor 1'] = s1['Actor 1']

for i1 in range(sheet1.shape[0]):
    for i2 in range(sheet2.shape[0]):
        if sheet1['Title'][i1] == sheet2['Title'][i2]:
            if sheet2['Actor 1'][i2] == "NO MESSAGE":
                sheet2['Actor 1'][i2] = sheet1['Actor 1'][i1]
                break
        
# sheet3 = sheet2.drop(index,axis=1)
writer = pd.ExcelWriter('newSheet2.xlsx', engine='xlsxwriter')
sheet2.to_excel(writer) 
writer.save()

# print(sheet2)        
        
        
        # print(sheet2['Title'][i1])
    # print(s1.loc['Title'])
    # x=type(s1)
# print(x)
# print(sheet2['Actor 1'][4])
# print(data.loc['Genres'])
# print(type(data))
# print(type(template1))
# print(data.length)    


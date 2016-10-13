import pandas as pd
xl = pd.ExcelFile('Data.xlsx')
df = xl.parse("Sheet1")
arr = df.values
for i in range(0, 39):
  print arr[i][1],":",arr[i][4]

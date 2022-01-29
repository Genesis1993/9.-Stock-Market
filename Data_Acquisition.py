import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from fastquant import get_pse_data

#http://www.pseapi.com/ - go to this site for the details of API
# /Stock/{symbol}/{date}
# /Stock/{symbol}/{From-Date}/{To-Date}
# /Stock/{symbol}
# /Stock/{symbol}/prices/{From-Date}/{To-Date}
#http://pseapi.com/api/Stock/JFC/03-15-2017

#Start and End Date
Start = "2020-01-01"
End = "2020-10-01"

PSEdata = get_pse_data("DITO","2020-08-01", "2020-10-25")
print(PSEdata.head())

DataToExcel = pd.ExcelWriter("DataFromPSE.xlsx", engine='xlsxwriter')
PSEdata.to_excel(DataToExcel,sheet_name="Sheet1")
DataToExcel.save()
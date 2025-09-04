import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"   
    r"SERVER=localhost,1433;"                   #注意用原始字符串 r"..."
    r"DATABASE=AdventureWorks2019;"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"               # 本机无证书时避免加密报错；不想加密也可用 Encrypt=no
)

query = open('../SQL Queries/Q1,3 Sales by Country Name.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df)

# Stacked horizontal bar chart for Sales by Country
Y_axis = np.arange(len(df['CountryName']))
plt.barh(df['CountryName'],df['Sales_LastYear'], 
        label = 'Last Year', color='steelblue')
plt.barh(df['CountryName'],df['Sales_YTD'],left = df['Sales_LastYear'],
        label='Year To Date', color='mediumseagreen')
plt.xticks(ticks = [0,10000000,20000000,30000000,40000000,50000000],
          labels = ["0M","$10M","$20M","$30M","$40M","$50M"])
plt.yticks(Y_axis, df['CountryName'])  
plt.xlabel("Sales")
plt.ylabel("Country")
plt.title("Sales by Country")
plt.legend()
plt.tight_layout()
plt.grid(axis = "x",linestyle = '--', linewidth = 0.5)
plt.gca().invert_yaxis()
plt.show()
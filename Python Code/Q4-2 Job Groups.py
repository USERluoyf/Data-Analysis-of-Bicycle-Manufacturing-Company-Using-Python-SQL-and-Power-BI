import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"   
    r"SERVER=localhost,1433;"                   #注意用原始字符串 r"..."
    r"DATABASE=AdventureWorks2019;"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"               # 本机无证书时避免加密报错；不想加密也可用 Encrypt=no
)

query = open('../SQL Queries/Q4 - Sick Leave by Job Group.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head(60))
plt.axvline(x=45,linestyle = '--',c= 'grey')
for x in list(set(df['OrganizationLevel']))[::-1]:
    df_1 = df[df['OrganizationLevel']==x]
    plt.barh(df_1['Job_Group'],df_1['Sick_Leave'],label = x,xerr=df_1['Deviation'])

plt.plot(0,0,label = 'error bars',c = 'black')
plt.xlabel('Annual Sick Leave (Hours)')
plt.ylabel('Job Group')
plt.title("Average Sick Leave by Job Group")
plt.xticks(ticks = [0,10,20,30,40,50,60,70])
plt.grid(axis = 'x',linestyle = '--', linewidth = 0.5)
plt.legend(bbox_to_anchor=(1.01, 0.4), loc='upper left', title = 'Organisation Lvl')
plt.tight_layout()
plt.show()
import pandas
import pymysql
con=pymysql.connect(host='bixxegmwtl9a9xkbdrih-mysql.services.clever-cloud.com',user='uzyalmtlztnwutid',password='CDbYfQLWfmGBX1ZU3Uh2',database='bixxegmwtl9a9xkbdrih')
# curs=con.cursor()
df=pandas.read_sql("select * from accounts",con)
print(df)
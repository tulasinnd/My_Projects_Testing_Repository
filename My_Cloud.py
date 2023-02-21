import pymysql
import pandas as pd
import csv
import os
# import mysql.connector
import time
import streamlit as st 
import plotly.graph_objects as go


# Master username
# admin
# Master password
# 12345phone
# Endpoint
# database-1.cazjp4zi8ncb.ap-northeast-1.rds.amazonaws.com

conn=pymysql.connect(
    host='database-1.cazjp4zi8ncb.ap-northeast-1.rds.amazonaws.com',
    user='admin',
    password='12345phone'
)

mycursor=conn.cursor()
mycursor.execute('select version()')
data=mycursor.fetchone()

# sql='''CREATE DATABASE PhonepeDB'''
# mycursor.execute(sql)

sql='''USE PhonepeDB'''
mycursor.execute(sql)

#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
# sql= "CREATE TABLE Data_Aggregated_Transaction_Table (MyIndex INT NOT NULL AUTO_INCREMENT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,Quarter INT,Year INT,State INT,PRIMARY KEY (MyIndex))"
# mycursor.execute(sql)
# print('Table created successfully.')
# conn.commit()
# df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_Transaction_Table.csv')
# for index, row in df.iterrows():
#      quer="INSERT INTO PhonePe_Database.Data_Aggregated_Transaction_Table(Payment_Mode,Total_Transactions_count,Total_Amount,Quarter,Year,State) values(%s,%s,%s,%s,%s,%S)"
#      mycursor.execute(quer,(row.Payment_Mode,row.Total_Transactions_count,row.Total_Amount,row.Quarter,row.Year,row.State))

#quer="INSERT INTO PhonepeDB.Data_Aggregated_Transaction_Table(Payment_Mode,Total_Transactions_count,Total_Amount,Quarter,Year,State) values(%s,%s,%s,%s,%s,%s)"%('other','150','15236','4','2022','22')
# sql = """INSERT INTO Data_Aggregated_Transaction_Table(
#    Payment_Mode,Total_Transactions_count,Total_Amount,Quarter,Year,State)
#    VALUES ('other',150,15236,4,2022,22)"""
# mycursor.execute(sql)
# print('DataFrame Inserted successfully.')
# conn.commit()

sql='select * from Data_Aggregated_Transaction_Table '
mycursor.execute(sql)
mode=mycursor.fetchall()
print(mode)
#mycursor.close()
st.title(':blue[PhonePe Pulse Data(2018-2022):signal_strength:]')
st.write("### **:blue[PhonePe India]**",mode)








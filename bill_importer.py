import pyodbc
import pandas
from datetime import datetime
import csv_analyser

def read_all_records():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-HKSJH39;'
                        'Database=FinAnalysis;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute("select * from MonthlyCredit")

    for record in cursor:
        print(record)


def upload_to_db(fileFullPath):
    filename, df = csv_analyser.read_bills(fileFullPath)

    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-HKSJH39;'
                        'Database=FinAnalysis;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()
    dtformat = r'%d/%m/%Y'

    for index, row in df.iterrows():
        dateStr = row['Date']
        dateEnteredStr = row['Date entered']
        referenceStr = row['Reference']
        descriptionStr = row['Description']
        amountStr = row['Amount']
        
        cursor.execute('insert into MonthlyCredit values(?,?,?,?,?,?)', 
        datetime.strptime(dateStr, dtformat),
        datetime.strptime(dateEnteredStr, dtformat),
        referenceStr,
        descriptionStr,
        float(amountStr),
        filename)

    cursor.commit()
    # cursor.execute("select * from MonthlyCredit")

    # for record in cursor:
    #     print(record)


def main():
    print('Works')
    #read_all_records()
    # upload_to_db(r'C:\Users\chann\Documents\CreditBills\Jan2021.csv')
    # upload_to_db(r'C:\Users\chann\Documents\CreditBills\Feb2021.csv')
    # upload_to_db(r'C:\Users\chann\Documents\CreditBills\Mar2021.csv')
    # upload_to_db(r'C:\Users\chann\Documents\CreditBills\Apr2021.csv')
    # upload_to_db(r'C:\Users\chann\Documents\CreditBills\May2021.csv')
    # upload_to_db(r'C:\Users\chann\Documents\CreditBills\Jun2021.csv')
    upload_to_db(r'C:\Users\chann\Documents\CreditBills\H2_2021\Aug2021.csv')



if __name__ == '__main__':
    main()
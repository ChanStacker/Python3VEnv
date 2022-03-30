import pandas as pd
import os
from datetime import datetime

def read_bills(fileFullPath):
    fileName = os.path.split(os.path.splitext(fileFullPath)[0])[1]
    print(fileName)
    df = pd.read_csv(fileFullPath, converters={'Date': str.strip})
    return fileName, df


def main():
    df = read_bills(r"C:\Users\chann\Documents\CreditBills\Test\Jan2021_Test.csv")
    print(df.head())
    # for index, row in df.iterrows():
    #     print(row['Description'], row['Amount'])
    print(df[['Description', 'Reference']])
    print(df.iloc[0])
    dtformat = r'%d/%m/%Y'
    #2021-06-20 18:33:10.8500000
    datestr = df.iloc[0]['Date']
    print('datestr is ' + datestr)
    theTime = datetime.strptime(datestr, dtformat)
    print(theTime)
    print(type(theTime))
    # onlyDesc = df.groupby('Description')
    # print(onlyDesc.sum())

if __name__ == "__main__":
    main()
import pandas as pd
import openpyxl
import os.path

def get_data_from_sheet_to_df(sheet_number):    
    rbi_df = pd.read_excel('../../PaymentsData.xlsx', sheet_number, skiprows = 5, nrows = 30, usecols = 'B:E')
    rbi_df.columns = ['RTGS Vol', 'RTGS Val', 'NEFT Vol', 'NEFT Val']
    rbi_df[rbi_df.columns] = rbi_df[rbi_df.columns].apply(pd.to_numeric, errors='coerce')
    # print(rbi_df.columns)
    print(rbi_df.head(5))

def begin_month_execution():
    sheet_number = 0
    get_data_from_sheet_to_df(sheet_number)

get_data_from_sheet_to_df() 

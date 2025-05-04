import openpyxl
import os.path

from datetime import datetime
import pandas as pd

import constants

def get_data_from_sheet_to_df():
    sheet_number = 0
    sheet_to_df_rbi(sheet_number)
    # sheet_to_df_npci(sheet_number)


def sheet_to_df_rbi(sheet_number):
    print(f"About to read the excel file at time : {datetime.now().strftime('%H:%M:%S')}\n\n")
    rbi_df = pd.read_excel(constants.PAYMENT_DATA_FILE_PATH, sheet_number, skiprows = 5, nrows = 31, usecols = constants.RBI_OPERATED_PAYMENTS_METHODS_COLS)
    print(f"Finished reading the excel file at time : {datetime.now().strftime('%H:%M:%S')}\n\n")
    rbi_df.columns = ['RTGS Vol', 'RTGS Val', 'NEFT Vol', 'NEFT Val']
    rbi_df[rbi_df.columns] = rbi_df[rbi_df.columns].apply(pd.to_numeric, errors='coerce')
    # print(rbi_df.columns)
    print(f"About to print the df at time : {datetime.now().strftime('%H:%M:%S')}")
    print(rbi_df.head(5))
    print(f"Finished printing the df at time : {datetime.now().strftime('%H:%M:%S')}")
    print(f"the size of the df is : {len(rbi_df.index)}")
    return rbi_df

def sheet_to_df_npci(sheet_number):
    npci_df = pd.read_excel(constants.PAYMENT_DATA_FILE_PATH, sheet_number, skiprows = 5, nrows = 31, usecols = constants.NPCI_OPERATED_PAYMENTS_METHODS_COLS)

    npci_df.columns = [
        'AePS Vol', 'AePS Val',
        'UPI Vol', 'UPI Val',
        'IMPS Vol', 'IMPS Val',
        'NACH Credit Vol', 'NACH Credit Val',
        'NACH Debit Vol', 'NACH Debit Val',
        'NETC Vol', 'NETC Val',
        'BBPS Vol', 'BBPS Val',
        'CTS Vol', 'CTS Val',
        'NFS Vol', 'NFS Val',
        'AePS (through micro-ATMs / BCs) Vol', 'AePs (through micro-ATMs / BCs) Val'
    ]

    npci_df[npci_df.columns] = npci_df[npci_df.columns].apply(pd.to_numeric, errors='coerce')
    # print(rbi_df.columns)
    print(npci_df.head(5))
    return npci_df

def begin_month_execution():
    get_data_from_sheet_to_df()

begin_month_execution()

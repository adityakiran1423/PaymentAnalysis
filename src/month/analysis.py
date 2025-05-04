import pandas as pd
import openpyxl
import os.path
from ... import constants

def get_data_from_sheet_to_df(sheet_number):
    sheet_to_df_rbi()
    sheet_to_df_npci()


def sheet_to_df_rbi(sheet_number):
    rbi_df = pd.read_excel(constants.PAYMENT_DATA_FILE_PATH, sheet_number, skiprows = 5, nrows = 30, usecols = constants.RBI_OPERATED_PAYMENTS_METHODS_COLS)
    rbi_df.columns = ['RTGS Vol', 'RTGS Val', 'NEFT Vol', 'NEFT Val']
    rbi_df[rbi_df.columns] = rbi_df[rbi_df.columns].apply(pd.to_numeric, errors='coerce')
    # print(rbi_df.columns)
    print(rbi_df.head(5))

def sheet_to_df_npci(sheet_number):
    npci_df = pd.read_excel(constants.PAYMENT_DATA_FILE_PATH, sheet_number, skiprows = 5, nrows = 30, usecols = constants.NPCI_OPERATED_PAYMENTS_METHODS_COLS)
    npci_df.columns = ['RTGS Vol', 'RTGS Val', 'NEFT Vol', 'NEFT Val']
    npci_df[npci_df.columns] = npci_df[npci_df.columns].apply(pd.to_numeric, errors='coerce')
    # print(rbi_df.columns)
    print(npci_df.head(5))

def begin_month_execution():
    # sheet_number = 61
    sheet_number = 0
    get_data_from_sheet_to_df(sheet_number)

begin_month_execution()

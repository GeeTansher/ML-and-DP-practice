import pandas as pd
import win32com.client as win32
import numpy as np
from pathlib import Path
import sys
import pythoncom
import logging
import time

pythoncom.CoInitialize()
win32c = win32.constants
logging.basicConfig(level=logging.DEBUG)


def convert_xls_to_xlsx(inP, outP) -> None:
    df = pd.read_excel(inP)
    df.to_excel(outP, index=False, header=True)


input_file = Path(r'C:\Data\Python and OpenCV\Excel pivot table automation\python\dataset\EXCEL_TOTAL0.9209643441939586.xls')
output_file = Path(r'C:\Data\Python and OpenCV\Excel pivot table automation\python\dataset\output.xlsx')

convert_xls_to_xlsx(input_file, output_file)


# read_file = pd.read_excel ("dataset/output.xlsx")

df = pd.read_excel ("C:\Data\Python and OpenCV\Excel pivot table automation\python\dataset\output.xlsx", skiprows=4)
df = df.drop(df.columns[[0, 1]], axis=1)
df = df.dropna(how='all', axis=1)
df = df.dropna(how='any', axis=0)
df["Sub Station"] = ""
df['Account No'] = df['Account No'].map(int)

print(df.shape[0], df.shape[1])
# df.head()

# master file
read_file1 = pd.read_excel("C:\Data\Python and OpenCV\Excel pivot table automation\python\dataset\MD_REPORT_0623_BD AGAIN.xlsx"
                           , sheet_name='MD_REPORT_0623_BD'
                           , usecols=["ACCOUNTNO","SUBSTATION"])
# read_file1.head()


read_file1["Account No"] = read_file1["ACCOUNTNO"]
read_file1["Sub Station"] = read_file1["SUBSTATION"]
read_file1 = read_file1.drop(read_file1.columns[[0,1]], axis=1)
read_file1['Account No'] = read_file1['Account No'].map(int)
# read_file1.head()


print(read_file1.shape[0], read_file1.shape[1])




Left_join = pd.merge(df, read_file1, on ='Account No', how ='left')
# Left_join.head()


Left_join["Sub Station"] = Left_join["Sub Station_y"]
Left_join = Left_join.drop('Sub Station_x', axis=1)
Left_join = Left_join.drop('Sub Station_y', axis=1)
# Left_join.head()


# write the csv file to xlsx File to create Pivot Table
Left_join.to_excel("C:\Data\Python and OpenCV\Excel pivot table automation\python\dataset\leftJoin.xlsx", sheet_name = 'leftJoin', index = False)



def pivot_table(wb: object, ws1: object, pt_ws: object, ws_name: str, pt_name: str, pt_rows: list, pt_cols: list, pt_filters: list, pt_fields: list):
    """
    wb = workbook1 reference
    ws1 = worksheet1 that contain the data
    pt_ws = pivot table worksheet number
    ws_name = pivot table worksheet name
    pt_name = name given to pivot table
    pt_rows, pt_cols, pt_filters, pt_fields: values selected for filling the pivot tables
    """

    # pivot table location
    pt_loc = len(pt_filters) + 2
    
    # grab the pivot table source data
    pc = wb.PivotCaches().Create(SourceType=win32c.xlDatabase, SourceData=ws1.UsedRange)
    
    # create the pivot table object
    pc.CreatePivotTable(TableDestination=f'{ws_name}!R{pt_loc}C1', TableName=pt_name)

    # selecte the pivot table work sheet and location to create the pivot table
    pt_ws.Select()
    pt_ws.Cells(pt_loc, 1).Select()

    # Sets the rows, columns and filters of the pivot table
    for field_list, field_r in ((pt_filters, win32c.xlPageField), 
                                (pt_rows, win32c.xlRowField),
                                (pt_cols, win32c.xlColumnField)):
        for i, value in enumerate(field_list):
            pt_ws.PivotTables(pt_name).PivotFields(value).Orientation = field_r
            pt_ws.PivotTables(pt_name).PivotFields(value).Position = i + 1

    # Sets the Values of the pivot table
    for field in pt_fields:
        pt_ws.PivotTables(pt_name).AddDataField(pt_ws.PivotTables(pt_name).PivotFields(field[0]), field[1], field[2]).NumberFormat = field[3]

    # Visiblity True or Valse
    pt_ws.PivotTables(pt_name).ShowValuesRow = True
    pt_ws.PivotTables(pt_name).ColumnGrand = True


def run_excel(f_path: Path, f_name: str, sheet_name: str):

    # filename = f_path / f_name
    filename = f_path

    # create excel object
    excel = win32.gencache.EnsureDispatch('Excel.Application')

    # excel can be visible or not
    excel.Visible = True  # False
    
    # try except for file / path
    try:
        wb = excel.Workbooks.Open(filename)
    except pythoncom.com_error as e:
        if e.excepinfo[5] == -2146827284:
            print(f'Failed to open spreadsheet.  Invalid filename or location: {filename}')
        else:
            raise e
        sys.exit(1)

    # set worksheet
    ws1 = wb.Sheets(sheet_name)
    
    # Setup and call pivot_table
    pivot_table_name = 'pivot_table' + ((str)(time.time())).split('.')[0]
    ws2_name = pivot_table_name
    wb.Sheets.Add().Name = ws2_name
    ws2 = wb.Sheets(ws2_name)
    
    # update the pt_name, pt_rows, pt_cols, pt_filters, pt_fields at your preference
    pt_name = pivot_table_name  # pivot table name, must be a string
    pt_rows = ['Sub Station']  # rows of pivot table, must be a list
    pt_cols = ['Collection Date']  # columns of pivot table, must be a list
    pt_filters = []  # filter to be applied on pivot table, must be a list
    # [0]: field name [1]: pivot table column name [3]: calulation method [4]: number format (explain the list item of pt_fields below)
    # pt_fields = [['Sale OfEC / ED', 'Sum of Sale OfEC / ED', win32c.xlSum, '0'],  # must be a list of lists
                #  ['Europe', 'Total Sales in Europe', win32c.xlSum, '0'],
                #  ['Japan', 'Total Sales in Japan', win32c.xlSum, '0'],
                #  ['Rest of World', 'Total Sales in Rest of World', win32c.xlSum, '0'],
                #  ['Global', 'Total Global Sales', win32c.xlSum, '0']]
                
    pt_fields = [['Sale Of\nEC / ED', 'Sum of Sale OfEC / ED', win32c.xlSum, '0']]
    # calculation method: xlAverage, xlSum, xlCount
    pivot_table(wb, ws1, ws2, ws2_name, pt_name, pt_rows, pt_cols, pt_filters, pt_fields)
    wb.Save() # save the pivot table created
    wb.Close(True)
    excel.Quit()


def mainFunction():
    # sheet name for data
    sheet_name = 'leftJoin'  # update with sheet name from your file
    # file path
    # f_path = Path.cwd() / "dataset"  # file in current working directory
    
    f_path = Path(r'C:\Data\Python and OpenCV\Excel pivot table automation\python\dataset\leftJoin.xlsx')  # file located somewhere else
    # excel file
    f_name = 'leftJoin.xlsx' # change to your Excel file name
    
    # function calls
    run_excel(f_path, f_name, sheet_name)


mainFunction()

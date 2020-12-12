import openpyxl

def readData(sheetName, rowNum, columnNum):
    file = "Test_Data/data_file.xlsx"
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetName)
    return sheet.cell(row=rowNum, column=columnNum).value

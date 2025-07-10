import pandas as pd


def get_initiate_data(path="PyTest/Cart/Data/Initiate.ods",sheetname ="initiate_data"):
    df = pd.read_excel(path,engine='odf',sheet_name=sheetname)
    cols = df.columns.to_list()
    headers = ','.join([col.strip() for col in cols])
    list_rows = []
    for _,row in df.iterrows():
        count = 0
        row_list = []
        while count < len(cols): 
            try:
                row_list.append(row[count].strip())
            except:
                row_list.append(row[count])
            count +=1
        list_rows.append(tuple(row_list))
    print(list_rows)
    return list_rows

def get_initiate_cols(path="PyTest/Cart/Data/Initiate.ods",sheetname ="initiate_data"):
    df = pd.read_excel(path,engine='odf',sheet_name=sheetname)
    cols = df.columns.to_list()
    headers = ','.join([col.strip() for col in cols])
    return headers

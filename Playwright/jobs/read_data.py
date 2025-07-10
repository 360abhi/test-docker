from configparser import ConfigParser
import pandas as pd
import os

con = ConfigParser()
con.read('Playwright/jobs/app.properties')

class Read:

    URL = con.get('URL','app_url')
    JOB_TITLE = con.get('JOB','python_job')
    SCRAPER_EXCEL = con.get('FILE','scraper_excel')
    SCRAPER_SHEET = con.get('FILE','scraper_sheet')

    def excel_write(path:str,output:pd.DataFrame,sheetname:str):
        if os.path.exists(path):
            with pd.ExcelWriter(path,engine='openpyxl',mode='a',if_sheet_exists='new') as writer:
                output.to_excel(writer,sheet_name=sheetname)
                print(f"Excel appended for {sheetname}")
        else:
            with pd.ExcelWriter(path,engine='openpyxl') as writer:
                output.to_excel(writer,sheet_name=sheetname)
                print(f"Excel created with {sheetname}")
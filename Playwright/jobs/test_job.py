import sys
from pathlib import Path
root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))

from Playwright.jobs.pages.home import Home
from Playwright.jobs.logger import setup_logger
from playwright.sync_api import sync_playwright,expect
from Playwright.jobs.read_data import Read
import pandas as pd

def getDf(jobs:list) -> pd.DataFrame:

    df = {
        "Jobs": jobs
    }

    df = pd.DataFrame(df)
    Read.excel_write(Read.SCRAPER_EXCEL,df,sheetname=Read.SCRAPER_SHEET)

    return df

def getJobs():
    with sync_playwright() as p:
        logger = setup_logger()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        home = Home(page,logger)
        home.goto_url(Read.URL)
        home.search_job(Read.JOB_TITLE)
        jobs = home.get_jobs(num_jobs=45)
        getDf(jobs)
        # for i in range(len(jobs)):
        #     print(f"{i+1} : {jobs[i]}")
        browser.close()

if __name__ == "__main__":
    getJobs()

# Tests




from playwright.sync_api import Page
from Playwright.jobs.utils import Utils

class Home:

    search_field = "(//input[@class='suggestor-input '])[1]"
    find_jobs_btn = "//div[.='Search']"
    next_page = "//span[.='Next']"
    page_count = "//div[@id='jobs-list-header']/div/span"

    def __init__(self,page:Page,logger):
        self.logger = logger
        self.page = page
        self.paths = Utils(self.page,self.logger)

    def goto_url(self,url:str) -> None:
        try:
            self.page.goto(url)
            self.page.wait_for_selector(self.find_jobs_btn, state="visible")
            self.paths.append_to_docx("Playwright_Test")
            self.logger.info(f"Navigated to {url} successfully")
        except Exception as e:
            self.logger.error(f"Exception moving to {url} : {str(e)}")


    def search_job(self,job_title:str) -> None:
        try:
            self.page.fill(self.search_field,value=job_title)
            self.page.click(self.find_jobs_btn)
            self.logger.info(f"Entered job title as {job_title}")
        except Exception as e:
            self.logger.error(f"Exception entering {job_title}: {str(e)}")

    def get_jobs(self,num_jobs:int):
        jobs = []
        count = 0
        self.paths.append_to_docx("Playwright_Test")
        for x in range(num_jobs):
            if x+1 in [20,40,60,80,100]:
                self.page.click(self.next_page)
                self.paths.append_to_docx("Playwright_Test")
                count = 0
                while True:
                    page_count_text = self.page.inner_text(self.page_count)[:2]
                    if page_count_text == str(x+2):
                        break
            try:
                job = self.page.inner_text(f"(//div[@class='srp-jobtuple-wrapper']/div/div/h2/a)[{count+1}]")
                self.logger.info(f"Successfully scraped job for {count+1}")
            except Exception as e:
                self.logger.error(f"Failed to scrape job for {count+1}")
            count += 1
            jobs.append(job)
        return jobs
    

            


        

FROM mcr.microsoft.com/playwright/python:v1.44.0

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

CMD ["pytest","Playwright/jobs/test_play.py","--reports=Playwright/jobs/report.html"]
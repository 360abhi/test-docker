FROM mcr.microsoft.com/playwright/python:v1.44.0

WORKDIR /app

# Only copy requirements first to cache the pip install layer
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

# Now copy the rest of the code (this is the layer that changes often)
COPY . .

CMD ["pytest", "Playwright/jobs/test_play.py", "--html=Playwright/jobs/report.html"]

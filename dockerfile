FROM python:3.9

# RUN apt update
RUN apt-get update && apt-get install vim -y --no-install-recommends




# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99





WORKDIR /app

RUN mkdir -p /app
COPY default/requirements.txt /app/
RUN pip install -r /app/requirements.txt --cache-dir /app/pip_cache

RUN mkdir -p /app/docker
RUN mkdir -p /app/docker/django
COPY docker/django/ /app/docker/django/

RUN mkdir -p /app/screenshots
RUN mkdir -p /app/csv

RUN mkdir -p /app/default
COPY default/ /app/default

RUN chown -R www-data:www-data /app

CMD ["python", "/app/default/scrape.py"]
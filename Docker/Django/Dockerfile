#############################################################
# AEYE Web Django Dockerfile
# Created By Yoonchul Chung
# Created At 2024.08.03
# Welcome to Visit Github : https://github.com/Yoonchulchung
#############################################################
FROM python:3.6-slim AS aeye_web_back

WORKDIR /app/

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS="yes"

#############################################################
# Dependencies
FROM aeye_web_back AS deps

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*

COPY dependencies_web.txt /app/
COPY dependencies_web_Back.txt /app/

RUN pip install --upgrade pip
RUN pip install -r dependencies_web.txt
RUN pip install -r dependencies_web_Back.txt
#############################################################
# Run
FROM deps AS runner

COPY /AEYE_Back_3_2/ /app/

# 포트 노출
EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

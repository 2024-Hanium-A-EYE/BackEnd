FROM python:3.6-slim AS aeye_web_back

WORKDIR /app


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

COPY dependencies.txt /app/
COPY dependencies_web_Back.txt /app/

RUN pip install --upgrade pip
RUN pip install -r dependencies.txt
RUN pip install -r dependencies_web_Back.txt

FROM deps AS runner
COPY AEYE_Back_3_2/* /app/

# 포트 노출
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

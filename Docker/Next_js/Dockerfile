FROM python:3.6-slim AS aeye_web_front

WORKDIR /app


FROM aeye_web_front AS deps

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY dependencies_web_Back.txt /app/

RUN pip install --upgrade pip
RUN pip install -r dependencies_web_Back.txt


FROM deps AS runner
COPY /AEYE_Back_3_2/* /app/

# 포트 노출
EXPOSE 8000

# 장고 서버 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
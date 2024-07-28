## 2024 한이음 AEYE 프로젝트
AEYE WEB BackEnd 서버 리포지토리 입니다.  
AWS EC2 인스턴스 안에서 빠르게 환경설정을 할 수 있도록 쉘을 작성하였습니다.  

| 작성된 쉘을 통해 자동으로 도커를 설치하고 도커 컨테이너 안에서 `Next.js`와 `Django`를 하나의 AWS EC2 인스턴스 안에서 쉽게 실행할 수 있습니다.  

브랜치 구성은 다음과 같이 구성되어 있습니다.  
```
main    : 프로젝트 테스트까지고 끝난 완성된 버전
test    : 코드 작성이 끝나고 테스트 중인 버전
develop : 코드 작성중인 버전 
```

**test 브랜치**에서는 `Github Actions`를 통해 CI가 진행되어 작성된 코드가 정의된 테스트 기준에 충족하는지 평가합니다.  



## 서버 환경
**Python** : 3.6  
**Django** : 3.2  
**djangorestframework** : 3.13.1  

Python 버전은 AI 서버가 요구하는 Tensorflow 버전이 파이선 3.6에서 동작이 가능하여 일관성을 위해 AEYE 프로젝트의 모든 Python 버전을 3.6으로 통일시켰습니다. Django 3.2는 파이선 3.6에서 동작 가능한 Django 버전이어서 Django 3.2 버전을 사용했습니다.  
 

## 서버 디렉토리 구성

```
BackEnd/ 
├── appspec.yml
├── BackEnd_automate.sh   # AWS EC2 인스턴스 초기화를 위한 쉘
├── dependencies.txt   # pip 설치를 위한 dependencies
├── LICENSE
├── README.md
└── AEYE_Back_3_2   # AEYE WEB Django 서버
    ├── db.sqlite3
    ├── manage.py
    ├── AEYE_Back_3_2
    └── data    # AEYE API 정의
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── urls.py
        ├── serializers.py
        ├── tests.py
        ├── views.py
        └── migrations
```

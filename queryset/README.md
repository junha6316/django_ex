

#참고
https://cocook.tistory.com/143

시작에 앞서 현재 디렉토리가 manage.py가 있는 디렉토리인지 확인 후 
아래 명령어 실행 부탁드립니다.

#가상환경 설치
pip install pipenv
pipenv shell
pipenv install -r ./requirements.txt

#실행하기전 아래 명령어를 실행시켜주세요
python manage.py makemigrations
python manage.py migrate

#db에 값을 넣는 명령어 
python manage.py seed_product
python manage.py seed_logs
python manage.py seed_canceled_logs

#python shell 실행
python manage.py shell
# SMS

python -m virtualenv env
env\Scripts\activate
pip freeze > requirements.txt
pip install -r requirements.txt
python -m pip install --upgrade pip

gcloud app deploy
gcloud auth login
gcloud app create
gcloud auth application-default login
gcloud config set project PROJECT_ID

cloud_sql_proxy -instances=salemterminal:asia-south1:iocsankari=tcp:3306

python manage.py makemigrations
python manage.py makemigrations polls
python manage.py migrate
python manage.py collectstatic

python manage.py runserver

python manage.py createsuperuser

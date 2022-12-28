# parse_weather
```sh
git clone https://github.com/IvanStored/parse_weather.git
cd parse_weather
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
docker run -d -p 6379:6379 redis
python manage.py qcluster
```

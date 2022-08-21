FROM python:3.9.8

COPY . /app

WORKDIR /app

RUN apt update && apt install -y unzip

RUN pip install -r requirements.txt

RUN unzip data.zip && python3 modelGenerator.py \
        && cp classifier.pkl featuresEncoder.sav scaler.sav /app/pregnancy_prediction/model_assets \
        && cd pregnancy_prediction \
        && python3 manage.py makemigrations && python3 manage.py migrate

COPY .env ./pregnancy_prediction/

WORKDIR /app/pregnancy_prediction

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]

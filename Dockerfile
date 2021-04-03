FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-2020-12-19

COPY requirements.txt /

RUN pip install -r /requirements.txt

ENV NLTK_DATA=/
# Sorry container size
RUN python -m textblob.download_corpora

COPY ./app /app/app

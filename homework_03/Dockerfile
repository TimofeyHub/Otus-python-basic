# команда для запуска контейнера
# docker run -p 8080:8000 -it homework

FROM python:3.10.12-bookworm

WORKDIR /homework_03

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000

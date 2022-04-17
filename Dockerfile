FROM python:3.8.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/home

ENV VIRTUAL_ENV=${APP_HOME}/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR $APP_HOME

EXPOSE 4848

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip &&\
    pip install -r requirements.txt &&\
    rm -rf /root/.cache/pip &&\
    rm requirements.txt

COPY ./data ${APP_HOME}/data
COPY ./app ${APP_HOME}/app
COPY ./.env ${APP_HOME}/.env

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4848", "--reload"]
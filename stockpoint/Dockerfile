FROM python:3.10-slim

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system --deploy

COPY . /app
CMD ["python", "app.py"]




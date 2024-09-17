FROM python:3.12.0-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev postgresql-dev libpq
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "saas.wsgi:application"]

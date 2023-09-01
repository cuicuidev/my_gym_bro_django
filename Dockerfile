FROM python:3.11.4

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn==21.2.0

EXPOSE 8000

CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]
FROM python:3-alpine
WORKDIR /app
COPY main.py main.py
COPY rickroll.pbz2 rickroll.pbz2
CMD python -u main.py


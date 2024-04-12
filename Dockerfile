FROM python:3.10-slim

COPY ./requirements.txt .

RUN python3 -m pip install virtualenv --no-cache-dir

RUN python3 -m virtualenv venv

RUN venv/bin/python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["venv/bin/python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

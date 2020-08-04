FROM python
WORKDIR /app

COPY ./requirements.txt /app

ENV PYTHONUNBUFFERED 1

RUN pip3 install --no-cache-dir -r requirements.txt


# really for ever file
# COPY ./main.py .
# COPY ./env.py .
COPY . .

# eviroments

# COPY .env .


CMD ["python", "main.py"]
# CMD ["python", "env.py"]
# CMD ["python", "-m", " discord", "--version"]

# CMD ["ping", "8.8.8.8"]

# CMD ['python', 'main.py']

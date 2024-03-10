FROM python:3.11.7
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY bot /bot
EXPOSE 5000
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN adduser --disabled-password webuser

USER webuser
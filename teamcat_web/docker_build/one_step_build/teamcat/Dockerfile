FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /web/www/teamcat
ADD requirements.txt /web/www/teamcat
ADD startup.sh /web/www/teamcat
WORKDIR /web/www/teamcat
RUN chmod 777 startup.sh
RUN pip install -r requirements.txt

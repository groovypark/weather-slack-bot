FROM python:3.7.2-slim-stretch
MAINTAINER soobin "soobin950@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
FROM python

RUN mkdir -p /code
ADD . /code
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_ENV='production'
ENV FLASK_RUN_HOST=0.0.0.0
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

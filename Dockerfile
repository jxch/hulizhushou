FROM python:3.10

RUN mkdir -p /code
ADD . /code
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_ENV='production'
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
RUN pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

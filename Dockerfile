FROM python:3.8.10
COPY . /usr/app/
EXPOSE 5001
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
CMD python app.py


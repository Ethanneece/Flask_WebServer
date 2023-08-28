# pull python image 
#
FROM python:slim

# copy requirements file into image. 
COPY ./requirements.txt /app/requirements.txt

# change working directory
WORKDIR /app

# install dependencies and packages in requirements file 
RUN pip install -r requirements.txt

# Copy local file content into image. 
COPY *.py /app
COPY concentration.timeseries.csv /app

ENTRYPOINT ["python"]

CMD ["app.py"]
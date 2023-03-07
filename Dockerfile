# python image
FROM python:3.9-buster

# setting work directory
WORKDIR /server

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copying requirements file to the cwd
COPY ./requirements.txt /server/requirements.txt

# installing requirements 
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# copying environment file
# COPY ./.env /server/
COPY ./.env /server/.env

# copying app folder
COPY ./app /server/app

# copying resources folder
COPY ./resources /server/resources


# exposing uvicorn port
EXPOSE 8000

# running app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
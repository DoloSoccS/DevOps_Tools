FROM python:3.10-alpine
# The docker OS image the application is using

WORKDIR ./app
# The starting directory when the app opens

COPY . /app
# Dependencies that need to be copied into the application

RUN python -m pip install -r requirements.txt
# Command line arguments that will execute once the container is running

EXPOSE 8080
# Used for opening ports

CMD python ./flaskApp.py
# Commands that are used to run the application. Different from run based on the time they are
# used
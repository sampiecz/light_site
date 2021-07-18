FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# The port this runs on
EXPOSE 8000

# Start django
CMD ["python3" ,"manage.py", "runserver", "0.0.0.0:8000"]

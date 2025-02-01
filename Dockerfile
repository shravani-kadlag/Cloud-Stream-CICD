FROM python:3

WORKDIR /data

# Install distutils (if necessary for your Python version)
RUN apt-get update && apt-get install -y python3-distutils

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

RUN python manage.py migrate

EXPOSE 8000

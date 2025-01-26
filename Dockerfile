FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your application
COPY . .

# Expose the port your app will run on
EXPOSE 8000

# Command to run your app (e.g., for Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

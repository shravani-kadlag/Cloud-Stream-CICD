# Use a Python 3.9 base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt . 

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the required port (replace 5000 with your app's port)
EXPOSE 8000

# Command to run your application (replace with your app's entry point)
CMD ["python", "todos/migrations/template/apps.py"]

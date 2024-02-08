# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Set the environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Define the command to run on container start
CMD ["python", "main.py"]

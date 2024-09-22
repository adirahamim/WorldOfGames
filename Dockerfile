FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y docker.io



# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py and Scores.txt files into the container at /app
#COPY MainScores.py /app
#COPY Scores.txt /app

# Make port 8777 available to the world outside this container
EXPOSE 5002

# Define environment variable
ENV NAME World

# Add a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl --fail http://localhost:8777/ || exit 1

# Run app.py when the container launches
#CMD ["python", "app.py"]
CMD ["python", "/app/MainScores.py"]


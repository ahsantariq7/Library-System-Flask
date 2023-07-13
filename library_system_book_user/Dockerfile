# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile ./

# Install pipenv
RUN pip install pipenv

# Install the project dependencies from the Pipfile
RUN pipenv install --system --skip-lock

# Copy the application code to the container
COPY . .

# Expose the port that the Flask application will run on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=src/app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

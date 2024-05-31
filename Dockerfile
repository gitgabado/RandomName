# Use the official lightweight Python image
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Install streamlit and other dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY . /app
WORKDIR /app

# Run the web service on container startup.
CMD ["streamlit", "run", "randomname.py", "--server.port=8080", "--server.address=0.0.0.0"]

# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY start.sh /start.sh

# Specify the command to run your bot.py script
CMD ["/bin/bash", "start.sh"]

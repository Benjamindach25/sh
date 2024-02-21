# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app
COPY start.sh /app/
# Specify the command to run your bot.py script
CMD ["/bin/bash", "start.sh"]

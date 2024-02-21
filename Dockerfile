# Use an official Python runtime as the base image
FROM python:3.8-slim
RUN apt install git
COPY start.sh /app/
# Specify the command to run your bot.py script
CMD ["/bin/bash", "start.sh"]

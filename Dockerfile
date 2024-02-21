FROM python:3.10.11
WORKDIR /app
RUN apt install update
RUN apt install upgrade -y
RUN apt install git -y
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]

FROM alejandromusic/my_ubuntu
WORKDIR /usr/src/app
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
CMD tail -f /dev/null

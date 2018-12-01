FROM node
MAINTAINER michael@csec.umiacs.umd.edu

RUN npm install -g @angular/cli
RUN npm update -g @angular/cli
ADD . /home/ATC-Station

WORKDIR /home/ATC-Station
RUN npm install
EXPOSE 4200

ENTRYPOINT [ "ng", "serve", "--host", " 0.0.0.0" ]
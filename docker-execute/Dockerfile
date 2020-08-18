FROM node:latest

# install python for LODStats
RUN apt-get update \
  && apt-get install -y python-pip python-dev librdf0-dev python-librdf librdf0-dev python-librdf git raptor2-utils

RUN pip install numpy
RUN pip install rdflib

RUN mkdir /LODStats \
  && cd /LODStats \
  && git clone https://github.com/AKSW/LODStats.git .

RUN cd /LODStats \
  && python setup.py install

# install git and nodejs for some scripts
#RUN apt-get update \
#  && apt-get install -y git-core curl build-essential openssl libssl-dev \
#  && git clone https://github.com/nodejs/node.git \
#  && cd node \
#  && ./configure \
#  && make \
#  && sudo make install



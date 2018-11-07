FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python-pip python-dev librdf0-dev python-librdf librdf0-dev python-librdf git raptor2-utils


RUN mkdir /LODStats \
  && cd /LODStats \
  && git clone https://github.com/AKSW/LODStats.git .

RUN cd /LODStats \
  && python setup.py install


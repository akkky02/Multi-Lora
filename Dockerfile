FROM ghcr.io/predibase/lorax:main

ENV MODEL mistralai/Mistral-7B-Instruct-v0.1
ENV VOLUME /data

RUN mkdir -p $VOLUME
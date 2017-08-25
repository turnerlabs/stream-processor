FROM stream-core
WORKDIR /opt/stream/
ADD . .
RUN mkdir /tmp/snaps/
CMD ["python", "index.py"]


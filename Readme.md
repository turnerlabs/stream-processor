# Stream Processor

* analyze many types of streams
* writes to a /tmp/ directory you specify or to /tmp/snaps/ if you dont'
* can pass in fps as FPS
* can pass in name as NAME
* can pass in stream as STREAM
* can pass in seconds to skip as SKIP

### example
```
export STREAM="https://www.youtube.com/watch?v=bgFSSPlzBl4"
export NAME="santa_1"
export FPS="2"
export SKIP="0"
docker-compose up
```

* This will write to a folder on your machine /tmp/santa_1
* the frames of the stream will be written as <frame>.png



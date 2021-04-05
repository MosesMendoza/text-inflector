#textblob-server

Run textblob as an API behind FastAPI in a docker container. Currently the only supported action is `tags` but more may be added. Contributions are welcome.

##Container
Builds on the FastAPI official container image from https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastap/ per the FastAPI [deployment docs](https://fastapi.tiangolo.com/deployment/docker)

Current image tag: python3.7-2020-12-19

##Textblob
Textblob is an NLP library written in Python. See docs

##Run tests
```
  python -m venv env
  . env/bin/activate
  pip install -r requirements_dev.txt
  python -m textblob.download_corpora
  pytest
```

##Build/run
```
  docker build -t textblob-server-image .
  docker run -d --name textblob-server-image -p <external port>:80 textblob-server
```

##Stop/destroy
```
  docker stop textblob-server
  docker rm textblob-server
```

##Endpoints
Tags
```
  Endpoint: /tags
  Action: POST
  Expected JSON body: '{"text": "<document text>"}'
  Response:
    { "tags": "[["I", "PRP"], ["am", "VBP"], ["a", "DT"], ["pear", "NN"]] }
```
Tags are parts of speech tags. See the [Penn treebank parts of speech](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)


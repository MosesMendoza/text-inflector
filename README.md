# textblob-server

Run textblob as an API behind FastAPI in a docker container. Currently the only supported action is `tags` but more may be added. Contributions are welcome. Note this doesn't do anything with certs/ssl/tls/https. Setting up your cluster for ssl termination isn't in scope here.

## Container
Builds on the FastAPI official container image from https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastap/ per the FastAPI [deployment docs](https://fastapi.tiangolo.com/deployment/docker) for Python 3.7.

Current image tag: python3.7-2020-12-19

## Textblob
Textblob is an NLP library written in Python. See [textblob docs](https://textblob.readthedocs.io)

Current Textblob version: 0.15.3

## Run tests

    python -m venv env
    . env/bin/activate
    pip install -r requirements_dev.txt
    python -m textblob.download_corpora
    pytest


## Build/run locally

    docker build -t textblob-server-image .
    docker run -d --name textblob-server -p 1234:80 textblob-server-image // (replace 1234 with the port you want the container to expose)


## Stop/destroy

    docker stop textblob-server
    docker rm textblob-server


## Endpoints
### Tags
Get the Parts of Speech tags for a given body of text. See the [Penn treebank parts of speech](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) for a map of tags/meanings.

    Endpoint: /tags
    Action: POST
    Example JSON body: '{"text": "I am a pear" }'
    Expected Response:
      { "tags": "[["I", "PRP"], ["am", "VBP"], ["a", "DT"], ["pear", "NN"]] }

Example:

    curl -X POST -H "Content-Type: application/json" -d '{"text": "I am a pear"}' http://localhost:1234/tags



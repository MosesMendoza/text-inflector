# text-inflector
[![CircleCI](https://circleci.com/gh/MosesMendoza/text-inflector.svg?style=shield)](https://circleci.com/gh/MosesMendoza/text-inflector)

Goal: a simple, lightweight service for:
- Generating parts of speech tags for a body of text
- Obtaining the form of a word given a parts of speech tag
- Obtaining basic tokenization of a given body of text (sentences)

This service doesn't have any logic other than to wrap APIs from TextBlob and Lemminflect. This runs [textblob](https://github.com/sloria/TextBlob) and [lemminflect](https://github.com/bjascob/LemmInflect) as APIs behind FastAPI in a docker container. The supported actions from textblob are `tags`, and `sentences`, but more may be added. The supported action from lemminflect is `getInflection`. Contributions are welcome. Note this doesn't do anything with certs/ssl/tls/https. Setting up a cluster for ssl termination isn't in scope here.

## Container
[temporary update]
The container logic has been rewritten to craft together a working version on Python 3.9. The previous logic (referenced below) uses the official container image(s) from FastAPI but Python 3.9 hasn't been added yet. As a result, building the container per instructions below will create a Python 3.9-based container. Documentation and code will be returned to the official versions after support is released.

Builds on the FastAPI official container image from https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ per the FastAPI [deployment docs](https://fastapi.tiangolo.com/deployment/docker) for Python 3.6.

Current image tag: python3.7-2020-12-19

## Textblob
Textblob is an NLP library written in Python. See [textblob docs](https://textblob.readthedocs.io). From Textblob: "TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more."[source](https://github.com/sloria/TextBlob)

Current Textblob version: 0.15.3

## Lemminflect
Lemminflect is an NLP library written in Python with a purpose of providing an English word inflection system. From Lemminflect: "LemmInflect uses a dictionary approach to lemmatize English words and inflect them into forms specified by a user supplied Universal Dependencies or Penn Treebank tag. The library works with out-of-vocabulary (OOV) words by applying neural network techniques to classify word forms and choose the appropriate morphing rules."[source](https://github.com/bjascob/LemmInflect) Lemminflect is one of a handful of libraries that will take a word and a Part of Speech tag and return a best effort at the form of that word corresponding to the supplied Part of Speech. See the [lemminflect repo](https://github.com/bjascob/LemmInflect).

Current Lemminflect version: 0.2.2

## Run tests

    python -m venv env
    . env/bin/activate
    pip install -r requirements_dev.txt
    python -m textblob.download_corpora
    pytest


## Build/run locally

    docker build -t text-inflector-image .
    docker run -d --name text-inflector -p 1234:80 text-inflector-image // (replace 1234 with the port you want the container to expose)


## Stop/destroy

    docker stop text-inflector
    docker rm text-inflector


## Endpoints
### Tags
Get the Parts of Speech tags for a given body of text. See the [Penn treebank parts of speech](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) for a map of tags/meanings.

    Endpoint: /tags
    Action: POST
    Example JSON body: '{"text": "I am a pear" }'
    Expected Response:
      { "tags": [["I", "PRP"], ["am", "VBP"], ["a", "DT"], ["pear", "NN"]] }

Example:

    curl -X POST -H "Content-Type: application/json" -d '{"text": "I am a pear"}' http://localhost:1234/tags

### Inflections
Get the inflected form of a word corresponding to a [Part of Speech](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) tag. Note that the supplied JSON body has required key (object) names (`word` and `pos`) per FastAPIs `Body` module.

    Endpoint: /inflections
    Action: POST
    Example JSON body: '{
      "word": {  "text": "pear" },
      "pos": { "tag": "NNS" }
    }'
    Expected Response:
      {'inflection': ['pears']}

Example:

    curl -X POST -H "Content-Type: application/json" -d '{ "word": {  "text": "pear" }, "pos": { "tag": "NNS" } }' http://localhost:1234/inflections

### Sentences
Get a list of sentences (strings) in a given body of text
    Endpoint: /sentences
    Action: POST
    Example JSON body:
      '{ "text": "I am a pear." }'
    Expected Response:
      '{ "sentences": ["I am a pear."] }'

Example:

    curl -X POST -H "Content-Type: application/json" -d '{"text": "I am a pear."}' http://localhost:1234/tokenizations

**textblob-server

Run tests
```
  python -m venv env
  . env/bin/activate
  pip install -r requirements_dev.txt
  python -m textblob.download_corpora
  pytest
```

Build
```
  docker build -t textblob-server .
```

Deploy
```
  docker build -t textblob-server-image .
  docker run -d --name textblob-server-image -p 3344:80 textblob-server
```

Stop/destroy
```
  docker stop textblob-server
  docker rm textblob-server
```

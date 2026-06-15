# functions-from-zero
Live Training
[![Python application test with Github Actions](https://github.com/riyazchougle/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/riyazchougle/functions-from-zero/actions/workflows/main.yml)

##To call Microservice
##something like this

curl -X 'POST' \
  'http://127.0.0.1:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'

### Build container
docker build --no-cache -t functions-from-zero  docker image ls
 docker run -p 127.0.0.1:8080:8080 functions-from-zero



### Invoke POST request
run invoke.sh


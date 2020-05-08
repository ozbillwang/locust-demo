# run locust test on api gateway with header `x-api-key`

### Usage

1. deploy serverless first

Make sure you have aws account and [set the AWS_PROFILE properly](set the AWS_PROFILE properly)

```
$ pushd serverless
$ npm install -g serverless
$ npm install
$ serverless deploy
$ popd
```

After deployed, you should see the api gateway url and its api key

If you missed the detail, you can run

```
$ sls info
Service Information
service: api-gateway-by-api-key
stage: dev
region: us-east-1
stack: api-gateway-by-api-key-dev
resources: 38
api keys:
  api-gateway-by-api-key-dev-api-key: PymRm7Hil4509Lj7yhbCP8haPVB7Qd9Sa3OskCjp
endpoints:
  POST - https://1ymxtrwh4e.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://1ymxtrwh4e.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://1ymxtrwh4e.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  PUT - https://1ymxtrwh4e.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  DELETE - https://1ymxtrwh4e.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  create: api-gateway-by-api-key-dev-create
  list: api-gateway-by-api-key-dev-list
  get: api-gateway-by-api-key-dev-get
  update: api-gateway-by-api-key-dev-update
  delete: api-gateway-by-api-key-dev-delete
layers:
  None
```
2. Update api key in file [locustfile.py](locustfile.py)

3. run the locust test

Make sure you have [installed locust](https://docs.locust.io/en/stable/installation.html)

```
locust
```

4. open browser with http://localhost:8089

host is the api server, in above sample, it is https://1ymxtrwh4e.execute-api.us-east-1.amazonaws.com



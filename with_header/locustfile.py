from locust import HttpLocust, TaskSet, between

# update the api key with real one
api_key = "M0wAqzfLRe2ZkX5SaYKqh8lDRic0X8bG6068x7LL"

def post(l):
    l.client.post("/dev/todos", json={"text": "Learn Serverless"}, headers={"x-api-key": api_key})

def get(l):
    l.client.get("/dev/todos", headers={"x-api-key": api_key})

class UserBehavior(TaskSet):
    tasks = {post: 2, get: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)

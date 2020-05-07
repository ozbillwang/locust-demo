from locust import HttpLocust, TaskSet, between

api_key = "PymRm7Hil4509Lj7yhbCP8haPVB7Qd9Sa3OskCjp"

def post(l):
    l.client.post("/dev/todos", json={"text": "Learn Serverless"}, headers={"x-api-key": api_key})

def get(l):
    l.client.get("/dev/todos", headers={"x-api-key": api_key})

class UserBehavior(TaskSet):
    tasks = {post: 2, get: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)

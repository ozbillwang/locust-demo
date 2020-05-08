from locust import HttpLocust, TaskSet, between

def post(l):
    l.client.post("/dev/todos", json={"text": "Learn Serverless"})

def get(l):
    l.client.get("/dev/todos")

class UserBehavior(TaskSet):
    tasks = {post: 2, get: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)

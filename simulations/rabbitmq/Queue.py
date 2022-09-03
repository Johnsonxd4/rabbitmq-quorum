import requests
from requests.auth import HTTPBasicAuth

class Queue:
    def __init__(self, url, vhost, user, pwd, queue_name):
        self.url = url
        self.vhost = vhost
        self.user = user
        self.pwd = pwd
        self.queue_name = queue_name

    def __get_basic_auth(self):
        return HTTPBasicAuth(self.user,self.pwd)

    def get_leader_name(self):
        response = requests.get(f'{self.url}/api/queues/{self.vhost}/{self.queue_name}',auth=self.__get_basic_auth())
        data = response.json()
        return data['leader']


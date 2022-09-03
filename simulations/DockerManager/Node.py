        
import docker
class Node:
    def __init__(self):
        self.docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        # self.docker_client = docker.from_env()
    
    def shutdwn_node(self,node_name):
        containers = self.docker_client.containers.list() 
        print(f'shutting down container {node_name}')
        container = [i for i in  containers if i.name.strip() == node_name.split('@')[1].strip()]
        print(len(containers))
        container[0].stop()

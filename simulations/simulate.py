import requests
from requests.auth import HTTPBasicAuth
import argparse
from rabbitmq.Queue import Queue
from DockerManager.Node import Node
api_url = 'http://localhost:8082'
username = 'mqadmin'
password = 'Admin123XX_'
vhost = '%2f'
def queue(args):
    
    node_manager = Node()
    
    if args.query_leader_of is not None:
        queue_manager = Queue(api_url,vhost,username,password,args.query_leader_of)
        print(queue_manager.get_leader_name())
    
    if args.shutdown_leader_of:
        queue_manager = Queue(api_url,vhost,username,password,args.shutdown_leader_of)
        leader_name =queue_manager.get_leader_name()
        print(f'current leader is {leader_name}. lets shutdown him')
        node_manager.shutdwn_node(leader_name)
        i = 1
        while i != 10:
            print(f'The new leader is {queue_manager.get_leader_name()}')
            i = i+1



parser = argparse.ArgumentParser(description='Program interation')
subparsers_queue = parser.add_subparsers(help='node leader action')

queue_parser = subparsers_queue.add_parser('queue',help='Queue Actions')
queue_parser.add_argument('--query-leader-of')
queue_parser.add_argument('--shutdown-leader-of')
queue_parser.set_defaults(func=queue)

args = parser.parse_args()
args.func(args)

#!/usr/bin/python3
"""
using a given REST API, for a given employee ID, returns information
about his/her TODO list progress
"""

from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    api_base_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'{api_base_url}/users/{employee_id}'
    todo_endpoint = f'{user_endpoint}/todos'
    filename = f'{employee_id}.json'

    user_data = requests.get(user_endpoint).json()

    todo_data = requests.get(todo_endpoint).json()

    user_tasks = []

    for todo_item in todo_data:
        task_data = {
            'task': todo_item.get('title'),
            'completed': todo_item.get('completed'),
            'username': user_data.get('username')
        }

        user_tasks.append(task_data)

    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({employee_id: user_tasks}))

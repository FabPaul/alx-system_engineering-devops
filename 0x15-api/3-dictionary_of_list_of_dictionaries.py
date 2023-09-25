#!/usr/bin/python3
"""
Export data from an API to JSON format.
"""
from json import dumps
import requests


def extract_employee_tasks(api_response, employee_info):
    """Extract tasks of an employee from API response.
    """
    employee_tasks = []

    for task in api_response:
        if task.get('userId') == employee_info.get('id'):
            task_data = {
                'username': employee_info.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            employee_tasks.append(task_data)

    return employee_tasks


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    users_endpoint = f'{base_url}/users'
    todos_endpoint = f'{base_url}/todos'
    output_filename = 'todo_all_employees.json'

    users_response = requests.get(users_endpoint).json()
    todos_response = requests.get(todos_endpoint).json()

    employees_tasks = {}

    for user_info in users_response:
        user_id = user_info.get('id')
        user_tasks = extract_employee_tasks(todos_response, {
            'id': user_id,
            'username': user_info.get('username')
        })
        employees_tasks[user_id] = user_tasks

    with open(output_filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(employees_tasks))

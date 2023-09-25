#!/usr/bin/python3
"""
using a given REST API, for a given employee ID, returns information
about his/her TODO list progress
"""

import requests
from sys import argv


def fetch_user_data(employee_id):
    """Fetch user data from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    response = requests.get(user_url)
    return response.json()


def fetch_todo_data(employee_id):
    """Fetch TODO list data for the user from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(todos_url)
    return response.json()


def calculate_task_progress(todos):
    """Calculate task progress statistics."""
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    non_completed_tasks = total_tasks - completed_tasks
    return total_tasks, completed_tasks, non_completed_tasks


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    user_data = fetch_user_data(employee_id)
    employee_name = user_data.get('name')

    todo_data = fetch_todo_data(employee_id)

    total_tasks, completed_tasks, non_completed_tasks = \
        calculate_task_progress(todo_data)

    print(f"Employee {employee_name} is done with tasks \
            ({completed_tasks}/{total_tasks}):")

    for todo in todo_data:
        if todo['completed']:
            print('\t', todo['title'])

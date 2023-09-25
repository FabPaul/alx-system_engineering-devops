#!/usr/bin/python3
"""
using a given REST API, for a given employee ID, returns information
about his/her TODO list progress
"""

import csv
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


def export_to_csv(employee_id, username, todos):
    """Export data to a CSV file."""
    filename = f'{employee_id}.csv'
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            status = todo.get('completed')
            title = todo.get('title')
            writer.writerow([employee_id, username, status, title])


if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    user_data = fetch_user_data(employee_id)
    username = user_data.get('username')

    todo_data = fetch_todo_data(employee_id)

    export_to_csv(employee_id, username, todo_data)

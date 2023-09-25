#!/usr/bin/python3
""" using a given REST API, for a given employee ID, returns information
about his/her TODO list progress
"""

import requests
import sys


def todo_list_progress(employee_id):
    """ Fetch and display the progress of an employee's TODO list """
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")

    user_data = user_response.json()
    employee_name = user_data["name"]

    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    print(f"Employee {employee_name} is done with tasks \
            ({completed_tasks}/{total_tasks}):")

    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list_progress(employee_id)

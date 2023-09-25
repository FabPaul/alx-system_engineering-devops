#!/usr/bin/python3
"""
using a given REST API, for a given employee ID, returns information
about his/her TODO list progress and exports it to a CSV file
"""

import csv
import requests
import sys


def todo_list_progress(employee_id):
    """ Fetch and display the progress of an employee's TODO list """
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")

    if user_response.status_code != 200:
        return

    user_data = user_response.json()
    employee_name = user_data["name"]

    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if todos_response.status_code != 200:
        return

    todos_data = todos_response.json()

    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            csv_writer.writerow([employee_id, employee_name,
                                todo["completed"], todo["title"]])

    print(f"Employee {employee_name}'s tasks have been exported to \
            {csv_file_name}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    todo_list_progress(employee_id)

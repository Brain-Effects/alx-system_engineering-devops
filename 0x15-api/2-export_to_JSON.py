#!/usr/bin/python3
"""
This script uses a REST API to fetch an employee's TODO list progress
and exports the data in JSON format.
"""

import json
import requests
import sys


def export_employee_todo_progress(employee_id):
    """
    Fetches an employee's TODO list progress using a REST API and exports it
    in JSON format.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    response = requests.get(user_url)
    user = response.json()
    response = requests.get(todos_url)
    todos = response.json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump({employee_id: tasks}, file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_progress(employee_id)

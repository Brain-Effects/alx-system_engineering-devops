#!/usr/bin/python3
"""
This module interacts with a REST API to retrieve and display the TODO list
progress of an employee based on their ID.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches an employee's TODO list progress using a REST API and prints it.

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

    done_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
          user.get('username'), len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

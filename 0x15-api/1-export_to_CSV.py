#!/usr/bin/python3
"""
This script uses a REST API to fetch an employee's TODO list progress
and exports the data in CSV format.
"""

import csv
import requests
import sys


def export_employee_todo_progress(employee_id):
    """
    Fetches an employee's TODO list progress using a REST API and exports it
    in CSV format.

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

    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user.get('name'), task.get(
                             'completed'), task.get('title')])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_progress(employee_id)

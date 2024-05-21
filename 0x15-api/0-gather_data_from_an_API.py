#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API and prints it to the standard output.
"""

import json
import requests
import sys


def get_employee_name(user_id):
    """Return the name of the employee by user ID."""
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    return user_response.json().get('name', None)


def get_employee_tasks(user_id):
    """Return the tasks of the employee by user ID."""
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    todos_response = requests.get(todos_url)
    return todos_response.json()


def print_employee_progress(user_id):
    """Print the employee's TODO list progress."""
    name = get_employee_name(user_id)
    tasks = get_employee_tasks(user_id)
    if not name or not tasks:
        print(f'Employee with ID {user_id} not found.')
        return

    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task['completed']]
    completed_count = len(completed_tasks)

    print(f'Employee {name} is done with tasks({completed_count}/'
          f'{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    print_employee_progress(user_id)

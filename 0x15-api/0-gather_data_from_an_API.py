#!/usr/bin/python3
"""
This module interacts with a REST API to retrieve and display the TODO list
progress of an employee based on their ID.
"""

import json
import requests
import sys


def get_employee_data(employee_id):
    """Fetch employee's name and TODO list progress using the
        given employee ID."""
    name_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = ('https://jsonplaceholder.typicode.com/todos?'
                 f'userId={employee_id}')

    name_response = requests.get(name_url)
    todos_response = requests.get(todos_url)

    if name_response.ok and todos_response.ok:
        name = name_response.json().get('name')
        todos = todos_response.json()
        return name, todos
    return None, None


def display_progress(name, todos):
    """Display the employee's TODO list progress."""
    total_tasks = len(todos)
    completed_tasks = sum(task.get('completed', False) for task in todos)

    print(f'Employee {name} is done with tasks({completed_tasks}/'
          f'{total_tasks}):')
    for task in todos:
        if task.get('completed', False):
            print(f'\t {task.get("title")}')


def main(employee_id):
    """Main function that processes the TODO list progress for
        a given employee ID."""
    name, todos = get_employee_data(employee_id)
    if name and todos:
        display_progress(name, todos)
    else:
        print(f'Employee with ID {employee_id} not found\
              or an error occurred.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ./0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    main(employee_id)

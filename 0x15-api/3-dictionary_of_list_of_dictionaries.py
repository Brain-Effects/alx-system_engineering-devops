#!/usr/bin/python3
"""
This script uses a REST API to fetch TODO list progress for all employees
and exports the data in JSON format.
"""

import json
import requests


def export_all_employees_todo_progress():
    """
    Fetches TODO list progress for all employees using a REST API and
    exports it in JSON format.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    users = users_response.json()

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_tasks = {}
    for user in users:
        user_tasks[user['id']] = [{
            "username": user['username'],
            "task": task['title'],
            "completed": task['completed']
        } for task in todos if task['userId'] == user['id']]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    export_all_employees_todo_progress()

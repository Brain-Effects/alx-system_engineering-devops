#!/usr/bin/python3
"""
This module contains a script to interact with the JSONPlaceholder API.
"""

import json  # Libraries imported in alphabetical order
import sys
from urllib import request

def get_employee_data(employee_id):
    """
    Function to get employee data from an API endpoint.
    """
    # Define the base URL and the API endpoints
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    try:
        # Send a GET request to the user API endpoint
        with request.urlopen(user_url) as u:
            user_data = json.loads(u.read().decode())
        with request.urlopen(todos_url) as u:
            todos_data = json.loads(u.read().decode())

        # Extract the employee name from the user data
        name = user_data.get('name')

        # Calculate the total number of tasks and the number of completed tasks
        total_tasks = len(todos_data)
        tasks = sum(1 for task in todos_data if task.get('completed'))

        # Print the first line of output
        print(f"Employee {name} is done with tasks({tasks}/{total_tasks}):")

        # Print the titles of completed tasks
        for task in todos_data:
            if task.get('completed'):
                print(f"\t {task.get('title')}")

    except Exception as e:
        print(f"Failed to get data, error: {str(e)}")


if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        # The first command-line argument is the employee ID
        employee_id = int(sys.argv[1])  # Convert the argument to an integer
        get_employee_data(employee_id)
    else:
        print("Usage: python3 todo_list_progress.py <employee_id>")

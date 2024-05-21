#!/usr/bin/python3
"""
This module contains a script to interact with the JSONPlaceholder API.
"""

import json
import requests
import sys


def get_employee_data(employee_id):
    """
    Function to get employee data from an API endpoint.
    """
    # Define the base URL and the API endpoints
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    # Send a GET request to the user API endpoint
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # If the requests were successful, status_code will be 200
    if user_response.status_code == 200 and todos_response.status_code == 200:
        # Load the data from the responses
        user_data = json.loads(user_response.text)
        todos_data = json.loads(todos_response.text)

        # Extract the employee name from the user data
        employee_name = user_data.get('name')

        # Calculate the total number of tasks and the number of completed tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task.get
                              ('completed'))

        # Print the first line of output
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/"
              f"{total_tasks}):")

        # Print the titles of completed tasks
        for task in todos_data:
            if task.get('completed'):
                print(f"\t {task.get('title')}")

    else:
        print(f"Failed to get data, status codes: "
              f"{user_response.status_code}, {todos_response.status_code}")


if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        # The first command-line argument is the employee ID
        employee_id = sys.argv[1]
        get_employee_data(employee_id)
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

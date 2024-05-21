#!/usr/bin/python3
"""
This module contains a script to interact with the JSONPlaceholder API.
"""

import csv  # Libraries imported in alphabetical order
import json
import sys
from urllib import request


def export_employee_data(employee_id):
    """
    Function to get employee data from an API endpoint and
    export it to a CSV file.
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

        # Extract the employee name and ID from the user data
        employee_name = user_data.get('username')
        user_id = user_data.get('id')

        # Open the CSV file for writing
        with open(f"{user_id}.csv", "w", newline="") as csvfile:
            fieldnames = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)

            # Write the data to the CSV file
            for task in todos_data:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": task.get('completed'),
                    "TASK_TITLE": task.get('title')
                })

    except Exception as e:
        print(f"Failed to get data, error: {str(e)}")


if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        # The first command-line argument is the employee ID
        employee_id = sys.argv[1]
        export_employee_data(employee_id)
    else:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")

#!/usr/bin/python3
"""
Script to retrieve information about an employee's TODO list progress using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    id_employee = int(sys.argv[1])
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_employee)
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id_employee)

    try:
        response_user = requests.get(url_user)
        response_todos = requests.get(url_todos)
        response_user.raise_for_status()
        response_todos.raise_for_status()

        user_data = response_user.json()
        todos_data = response_todos.json()

        employee_name = user_data.get('name')
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get('completed')]
        num_done_tasks = len(done_tasks)

        print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done_tasks, total_tasks))
        for task in done_tasks:
            print("\t{}".format(task.get('title')))

    except requests.exceptions.RequestException as e:
        print("Error:", e)


#!/usr/bin/python3
"""Returns to-do list information for a given employee ID"""
import requests
import sys

def fetch_todo_list(employee_id):
    """Fetches and returns TODO list information for the given employee ID."""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    # Fetch user data
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    user = response.json()
    employee_name = user.get("name")

    # Fetch TODO list data
    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)

    todos = response.json()
    return employee_name, todos

def print_todo_progress(employee_name, todos):
    """Prints the progress of completed tasks for the given employee."""
    completed_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee ID>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_name, todos = fetch_todo_list(employee_id)
    print_todo_progress(employee_name, todos)


#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url)
    if response.status_code == 200:
        tasks = response.json()
        total_tasks = len(tasks)
        done_tasks = [task for task in tasks if task["completed"]]
        total_done_tasks = len(done_tasks)
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()
        print("Employee {} is done with tasks({}/{}):".format(user["name"], total_done_tasks, total_tasks))
        for task in done_tasks:
            print("\t {}".format(task["title"]))
    else:
        print("No employee found for the given ID")
else:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))


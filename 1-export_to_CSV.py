#!/usr/bin/python3
import csv
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    user_data = user_response.json()
    employee_name = user_data['name']

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
    todo_data = todo_response.json()

    with open('{}.csv'.format(employee_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])


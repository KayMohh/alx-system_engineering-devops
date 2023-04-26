""" #!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

""" 
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



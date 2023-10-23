#!/usr/bin/python3
"""
    Exports data in the JSON format
"""


from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":

    userId = argv[1]
    user = get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    todos = get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        dump(todoUser, f)

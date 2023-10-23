#!/usr/bin/python3
"""
    Exports data in a Dictionary List of Dictionaries
"""


from requests import get
from json import dump


if __name__ == "__main__":

    users = get("https://jsonplaceholder.typicode.com/users")
    users = users.json()

    todos = get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees_dict_list_dict.json', mode='w') as f:
        dump(todoAll, f)

#!/usr/bin/python3
'''this module contains the function export_all'''
import json
import requests as req


def export_all_data():
    '''returns information for all employees in JSON format'''
    filename = 'todo_all_employees.json'
    users = req.get('https://jsonplaceholder.typicode.com/users/').json()
    todo = req.get('https://jsonplaceholder.typicode.com/todos').json()
    all_users = {}
    cur_user = {}

    for user in users:
        user_id = user.get('id')
        all_users[user_id] = []
        cur_user[user_id] = user.get('username')

    for task in todo:
        cur_task = {}
        user_id = task.get('userId')
        cur_task['task'] = task.get('title')
        cur_task['completed'] = task.get('completed')
        cur_task['username'] = cur_user.get(user_id)
        all_users.get(user_id).append(cur_task)

    with open(filename, 'w') as json_file:
        json.dump(all_users, json_file)


if __name__ == "__main__":
    export_all_data()

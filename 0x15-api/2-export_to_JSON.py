#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests as req
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = req.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()
    filename = user_id + '.json'

    with open(filename, "w") as jsonfile:
        json.dump({user_id: [{
                "task": tak.get("title"),
                "completed": tak.get("completed"),
                "username": username
            } for tak in todos]}, jsonfile)

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def main_root():
    return "welcome to the backend"


# to run this, prerequisits:
# pip install "fastapi[standard]

# command to run code:
# fastapi dev main.py

# note: code will run on localHost:8000
# main.py is the entry point of the application. refer to the docs, google or GPT and get the party started!
# env variables coming soon

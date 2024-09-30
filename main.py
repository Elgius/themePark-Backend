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

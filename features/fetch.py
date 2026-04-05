import requests

def fetch_data():
    try:
        status_code = requests.get("https://jsonplaceholder.typicode.com/todos/1").status_code
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
        return 404
    else:
        return status_code

print(fetch_data())

def get_data():
    print("This is my function to fetch the 1st todo...")
    return requests.get("https://jsonplaceholder.typicode.com/todos/1")

def get_todo():
    print("This is my function to fetch the 1st todo...")
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return res.json()
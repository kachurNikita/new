import requests

def greeting():
    response = requests.get('https://httpbin.org')
    return response.status_code


def  goodbye():
    return "Goodbye Boss"
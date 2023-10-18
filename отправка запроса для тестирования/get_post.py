import requests

r = requests.post('http://127.0.0.1:5000/testing', json={'questions_num':1})

print(r.text)

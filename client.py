import requests

HOST = 'http://127.0.0.1:8080'


# resp = requests.post(f'{HOST}/advs/', json={
#     'header': 'h1121',
#     'owner': 'own11121',
#     'description': '1dqweq1111112'
# })

# resp = requests.get(f'{HOST}/advs/')
# resp = requests.get(f'{HOST}/advs/13')
# resp = requests.get(f'{HOST}/advs/13')
# resp = requests.delete(f'{HOST}/advs/111111111')
resp = requests.delete(f'{HOST}/advs/13')

print(resp.status_code)
print(resp.text)

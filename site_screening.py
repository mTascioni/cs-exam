import requests

url = 'http://xss1.challs.cyberchallenge.it/report'
r = requests.get(url)
print("ricevuto: ", r.status_code)
print("cookies: ", r.cookies)

#Uso un cookie mio in una get
#cookies = {'my_cookie': 'cookie_value'}
#r = requests.get(url, cookies=cookies)
#print("ricevuto: ", r.status_code)

## POST
#p=requests.post('url', data={'key': 'value'})
#print("ricevuto: ", p.json())


# METODI DELETE, HEAD, OPTIONS
#r = requests.delete('https://httpbin.org/delete')
#r = requests.head('https://httpbin.org/get')
#r = requests.options('https://httpbin.org/get')


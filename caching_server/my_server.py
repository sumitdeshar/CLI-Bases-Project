import http.client
import json


def my_http(url:str, method:str, endpoint:str):
    print('url', url, 'method', method.upper(), 'endpoint', endpoint)
    server_url = 'dummyjson.com'
    connection = http.client.HTTPSConnection(url) # create connection

    connection.request(method=method.upper(), url=endpoint) #"/products"
    response = connection.getresponse()

    print(response.status, response.reason)
    data = json.loads(response.read().decode())
    connection.close()
    
    return data['products'][:5]

# my_http(url='dummyjson.com', method='get', event='/products')
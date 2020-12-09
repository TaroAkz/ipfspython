import ipfsApi

api = ipfsApi.Client('127.0.0.1', 5001)

print(api)

res = api.add('test.txt')

print(res['Hash'])


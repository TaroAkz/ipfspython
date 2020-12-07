import ipfsApi

api = ipfsApi.Client('127.0.0.1', 5001)

image = api.add('photo', match='*.png')

print(image)

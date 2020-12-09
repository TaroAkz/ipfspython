# ipfspython

#installation library ipfs
pip3 install ipfsapi

#create file python index.py
#coding
```python
import ipfsApi

api = ipfsApi.Client('127.0.0.1', 5001)
#Print out your Api
print(api)
res = api.add('test.txt')

#Go to terminal 
python3 index.py

#Result
<ipfsApi.client.Client object at 0x7feb751df070>

print(res)

#Go to terminal 
python3 index.py

#This is the result
{'Name': 'test.txt', 'Hash': 'QmY9cxiHqTFoWamkQVkpmmqzBrY3hCBEL2XNu3NtX74Fuu', 'Size': '14'}
```


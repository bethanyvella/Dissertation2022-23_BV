# WebScrapingProject

## Getting headers from Http Response
urllib.request.urlopen returns an object with an info() method which returns the headers:
```python
import urllib.request

response = urllib.request.urlopen("http://fr.wikipedia.org/wiki/Alan_Turing")
print(response.code)

info = response.info()
for header in info._headers:
    print(header)

response_content = response.read()
print(response_content)
```

## change useragent 
```python
import urllib.request
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
```

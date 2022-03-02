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

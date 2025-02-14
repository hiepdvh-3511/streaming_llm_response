import requests

url = "http://127.0.0.1:8001/stream"

with requests.get(url, stream=True) as response:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))  # Giải mã từ bytes về string

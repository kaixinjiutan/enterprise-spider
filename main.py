from core.client import HttpClient
headers = {
    "User-Agent": "Mozilla/5.0"
}

if __name__ == "__main__":
    client = HttpClient(headers=headers)
    html = client.get("https://httpbin.org/get")
    print("请求成功, 长度: ", len(html))
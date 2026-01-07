import time
import random
import requests
from typing import Optional

class HttpClient:
    """
    企业级HTTP客户端
    -超时控制
    -重试机制
    -基础反爬处理
    Docstring for HttpClient
    """

    def __init__(
            self,
            headers:dict,
            timeout: int = 10,
            max_retries: int = 3,
            sleep_range: tuple = (1, 3)
    ):
        self.headers = headers
        self.timeout = timeout
        self.max_retries = max_retries
        self.sleep_range = sleep_range
        self.session = requests.Session()

    def get(self, url: str, params: Optional[dict] = None) -> str:
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.session.get(
                    url = url,
                    headers = self.headers,
                    params = params,
                    timeout = self.timeout
                )

                if response.status_code == 200:
                    return response.text
                
                if response.status_code in (403, 429):
                    wait = random.uniform(*self.sleep_range)
                    print(f"[WARN]{response.status_code} 被限流, 第{attempt} 次重试， 休眠{wait:.1f}s")
                    time.sleep(wait)
                    continue
                print(
                    f"[ERROR] HTTP {response.status_code}, URL={url}"
                )
            except requests.RequestException as e:
                print(f"[ERROR] 请求异常， 第{attempt} 次重试: {e}")
            time.sleep(1)

        raise RuntimeError(f"请求失败， 超过最大重试次数: {url}")


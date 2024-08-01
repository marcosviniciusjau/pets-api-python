from typing import Dict # 3.8

class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None:
        self.body = body
        self.param = param

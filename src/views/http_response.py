class HttpResponse:
  def __init__(self, body: dict = None, status_code: int = 200) -> None:
    self.body = body
    self.status_code = status_code
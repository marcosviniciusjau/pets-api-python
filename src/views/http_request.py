class HttpRequest:
  def __init__(self, body: dict, param: dict = None) -> None:
    self.body = body
    self.param = param

  def get_body(self) -> dict:
    return self.body

  def get_param(self) -> dict:
    return self.param
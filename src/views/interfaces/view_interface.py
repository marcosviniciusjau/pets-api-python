from abc import ABC, abstractmethod

from src.views.http_request import HttpRequest
from src.views.http_response import HttpResponse


class ViewInterface(ABC):
  @abstractmethod
  def handle(self, http_request: HttpRequest) -> HttpResponse:
    pass
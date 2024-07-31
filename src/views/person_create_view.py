from src.controllers.interfaces.person_create_controller import PersonCreateControllerInterface
from src.views.http_request import HttpRequest
from src.views.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PersonCreateView(ViewInterface):
  def __init__(self, controller: PersonCreateControllerInterface) -> None:
    self.__controller = controller
  
  def handle(self, http_request: HttpRequest) -> HttpResponse:
    person_info = http_request.get_body()
    body_response = self.__controller.create(person_info)
    return HttpResponse(status_code=201, body=body_response)
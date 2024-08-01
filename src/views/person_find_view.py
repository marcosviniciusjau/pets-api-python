from src.controllers.interfaces.person_find_controller import PersonFindControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PersonFindView(ViewInterface):
  def __init__(self, controller: PersonFindControllerInterface) -> None:
    self.__controller = controller

  def handle(self,http_request: HttpRequest) -> HttpResponse:
    person_id = http_request.get_param("person_id")
    body_response = self.__controller.find(person_id)

    return HttpResponse(status_code=200, body=body_response)
  
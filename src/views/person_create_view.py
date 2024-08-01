from src.controllers.interfaces.person_create_controller import PersonCreateControllerInterface
from src.validators.person_create_validator import person_create_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PersonCreateView(ViewInterface):
    def __init__(self, controller: PersonCreateControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_create_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
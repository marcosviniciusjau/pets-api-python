from pydantic import BaseModel, constr, ValidationError
from src.errors.error_types.unprocessable_entity import UnprocessableEntity
from src.views.http_types.http_request import HttpRequest

def person_create_validator(http_request: HttpRequest) -> None:
   
   class BodyData(BaseModel):
      first_name: constr(min_length=1) # type: ignore
      last_name: constr(min_length=1) # type: ignore
      age: int = None
      pet_id: int

   try: 
      BodyData(**http_request.body)

   except ValidationError as e:
      raise UnprocessableEntity(e.errors()) from e

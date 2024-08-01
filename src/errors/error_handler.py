from src.errors.error_types.bad_request import BadRequest
from src.errors.error_types.not_found import NotFound
from src.errors.error_types.unprocessable_entity import UnprocessableEntity
from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
   if isinstance(error, (BadRequest, NotFound, UnprocessableEntity)):
     return HttpResponse(
          status_code=error.status_code,
           body={
              "errors": [{
                 "title": error.name,
                 "detail": error.message
              }]
            }
      )
   
   return HttpResponse(
      status_code=500,
      body={
         "errors": [{
            "title": "Internal Server Error",
            "detail": str(error)
         }]
       }
   )
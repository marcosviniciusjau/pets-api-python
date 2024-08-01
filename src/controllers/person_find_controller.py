from src.controllers.interfaces.person_find_controller import PersonFindControllerInterface
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.people_repos import PeopleReposInterface
import re
class PersonFindController(PersonFindControllerInterface):
  def __init__(self, person_repos:PeopleReposInterface) -> None:
    self.__person_repos = person_repos

  def find(self, person_id: int) -> dict:
    person = self.__find_in_db(person_id)
    response = self.__format_response(person)
    return response
  
  def find_in_db(self, person_id: int) -> PeopleTable:
    person = self.__person_repos.get_person(person_id)
    if not person:
      raise Exception("Pessoa não encontrada")
    return person

  def __format_response(self, person: PeopleTable) -> dict:
    return {
      "data": {
        "type": "Person",
        "id": person.id,
        "attributes": {
          "first_name": person.first_name,
          "last_name": person.last_name,
          "pet_name": person.pet_name,
          "pet_type": person.pet_type
        }
      }
    }
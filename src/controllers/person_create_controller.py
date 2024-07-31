from src.models.sqlite.interfaces.people_repos import PersonReposInterface
import re
class PersonCreateController:
  def __init__(self, person_repos:PersonReposInterface) -> None:
    self.__person_repos = person_repos

  def create(self, person_info: dict)-> dict:
     first_name = person_info["first_name"]
     last_name = person_info["last_name"]
     age = person_info["age"]
     pet_id = person_info["pet_id"]

     self.__validate_name(first_name, last_name)
     self.__insert_person(first_name, last_name, age, pet_id)
     formatted_response = self.__format_response(person_info)
     return formatted_response
 
  def __validate_name(self, first_name: str, last_name: str) -> None:
     non_valid_caracteres = re.compile(r'[^a-zA-Z]')

     if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
       raise Exception("Nome da pessoa inválido")
     else:
       return True
     
  def __insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
    self.__person_repos.insert_person(first_name, last_name, age, pet_id)

  def __format_response(self, person_info: dict) -> dict:
    return {
        "data":{
          "type": "Person",
          "count": 1,
          "attributes": person_info
        }
    }
      
  
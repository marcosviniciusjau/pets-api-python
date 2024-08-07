from typing import Dict
import re
from src.errors.error_types.bad_request import BadRequest
from src.models.sqlite.interfaces.people_repos import PeopleReposInterface
from .interfaces.person_create_controller import PersonCreateControllerInterface

class PersonCreateController(PersonCreateControllerInterface):
    def __init__(self, people_repos: PeopleReposInterface) -> None:
        self.__people_repos = people_repos

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person(first_name, last_name, age, pet_id)
        formated_response = self.__format_response(person_info)
        return formated_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise BadRequest("Nome da pessoa invalido!")

    def __insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repos.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
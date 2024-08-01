from typing import Dict, List
from src.models.sqlite.interfaces.pets_repos import PetsReposInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_list_controller import PetListControllerInterface

class PetListController(PetListControllerInterface):
    def __init__(self, pet_repos: PetsReposInterface) -> None:
        self.__pet_repos = pet_repos

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repos.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({ "name": pet.name, "id": pet.id })

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }
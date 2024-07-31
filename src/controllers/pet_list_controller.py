from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repos import PetsReposInterface

class PetListController:
  def __init__(self, pets_repos:PetsReposInterface) -> None:
    self.__pets_repos = pets_repos

  def list(self) -> list[PetsTable]:
    pets = self.__get_pets()
    response =  self.__format_response(pets)
    return response

  def __get_pets(self) -> list[PetsTable]:
    pets = self.__pets_repos.get_all_pets()
    return pets
  
  def __format_response(self, pets: list[PetsTable]) -> dict:
    formmatted_pets = []

    for pet in pets:
      formmatted_pets.append({
        "id": pet.id,
        "name": pet.name,
        "type": pet.type
      })
      
      return {
        "data":"Pets",
        "count": len(formmatted_pets),
        "attributes": formmatted_pets
      }
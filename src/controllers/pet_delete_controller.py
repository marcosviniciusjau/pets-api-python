from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repos import PetsReposInterface

class PetDeleteController:
  def __init__(self, pets_repos:PetsReposInterface) -> None:
    self.__pets_repos = pets_repos

  def delete(self, name:str) -> None:
    self.__pets_repos.delete_pets(name)
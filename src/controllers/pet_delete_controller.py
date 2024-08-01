from src.models.sqlite.interfaces.pets_repos import PetsReposInterface
from .interfaces.pet_delete_controller import PetDeleteControllerInterface

class PetDeleteController(PetDeleteControllerInterface):
    def __init__(self, pet_repos: PetsReposInterface) -> None:
        self.__pet_repos = pet_repos

    def delete(self, name: str) -> None:
        self.__pet_repos.delete_pets(name)
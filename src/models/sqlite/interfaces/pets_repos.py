from abc import ABC, abstractmethod

from src.models.sqlite.entities.pets import PetsTable

class PetsReposInterface(ABC):
  @abstractmethod
  def get_all_pets(self) -> list[PetsTable]:
    pass

  @abstractmethod
  def delete_pets(self, name:str) -> None:
    pass
from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import PetsTable

class PetListControllerInterface(ABC):

  @abstractmethod
  def list(self) -> list[PetsTable]:
    pass
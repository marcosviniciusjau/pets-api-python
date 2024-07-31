from abc import ABC, abstractmethod

class PersonFindControllerInterface(ABC):
  @abstractmethod
  def find(self, person_id: int) -> dict:
    pass
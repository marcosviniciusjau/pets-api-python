from abc import ABC, abstractmethod

class PersonCreateControllerInterface(ABC):
  @abstractmethod
  def create(self, person_info: dict)-> dict:
   pass
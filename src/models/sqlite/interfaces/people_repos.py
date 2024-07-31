from abc import ABC, abstractmethod

from src.models.sqlite.entities.people import PeopleTable
class PersonReposInterface(ABC):
  @abstractmethod
  def insert_person(self, first_name, last_name, age, pet_id) -> None:
    pass

  @abstractmethod
  def get_person(self,person_id:int) -> PeopleTable:
    pass
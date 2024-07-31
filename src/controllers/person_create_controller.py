from src.models.sqlite.interfaces.people_repos import PersonReposInterface

class PersonCreateController:
  def __init__(self, person_repos:PersonReposInterface) -> None:
    self.__person_repos = person_repos

  def create_person(self, first_name, last_name, age, pet_id):
    self.person_repos.insert_person(first_name, last_name, age, pet_id)
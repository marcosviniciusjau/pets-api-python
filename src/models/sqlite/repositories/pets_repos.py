from src.models.sqlite.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.pets_repos import PetsReposInterface

class PetsRepos(PetsReposInterface):
  def __init__(self, db_connection):
    self.__db_connection = db_connection

  def get_all_pets(self)-> list[PetsTable]:
    with self.__db_connection as database:
      try:
        pets = database.query(PetsTable).all()
        return pets
      except NoResultFound:
        return []

  def delete_pets(self, name:str)->None:
    with self.db_connection_handler.session() as database:
      try:
        database.session.query(PetsTable).filter(PetsTable.name == name).delete()
        database.session.commit()
      except Exception as exception:
        database.session.rollback()
        raise exception
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.peope_repos import PeopleRepos

from src.controllers.person_find_controller import PersonFindController
from src.views.person_find_view import PersonFindView

def person_find_composer():
    model = PeopleRepos(db_connection_handler)
    controller = PersonFindController(model)
    view = PersonFindView(controller)

    return view
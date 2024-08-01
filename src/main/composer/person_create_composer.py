from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.peope_repos import PeopleRepos

from src.controllers.person_create_controller import PersonCreateController
from src.views.person_create_view import PersonCreateView

def person_create_composer():
    model = PeopleRepos(db_connection_handler)
    controller = PersonCreateController(model)
    view = PersonCreateView(controller)

    return view
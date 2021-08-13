
from api.models.drinks import Drink

from api.services.users import UserService

class DrinksService(UserService):
    def list_drinks(self):
        return Drink.objects.all()
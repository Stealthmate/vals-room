
from functools import wraps

from api.services import exceptions

def withStaff(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if self.user.django_user.is_staff:
            return f(self, *args, **kwargs)
        raise exceptions.NotAuthorizedException()
    return wrapper
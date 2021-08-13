
class ServiceException(Exception):
    pass

class ObjectNotFoundException(Exception):
    pass

class UserInvitationTokenConsumedException(ServiceException):
    pass

class NotAuthorizedException(Exception):
    pass
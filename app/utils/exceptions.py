class AveryException(Exception):
    """Base Avery application exception."""
    pass


class SkillNotFoundException(AveryException):
    """Raised when a requested skill is unavailable."""
    pass


class ServiceException(AveryException):
    """Raised when a backend service fails."""
    pass
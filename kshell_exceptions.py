class StandardException(Exception):
    """Base exception for KShell"""
    pass

class FieldNotProvidedError(StandardException):
    """Exception is raised when command fields are not provided by the user"""
    pass

class BaseNotSupportedError(StandardException):
    """Exception raised if base is not supported"""
    pass

class IncorrectIntegerBaseError(StandardException):
    """Exception raised if an integer has an incorrect base"""
    pass

class UnknownTypeError(StandardException):
    """Exception raised if a boolean or another type is unknown"""
    pass

class ProjectFilesError(StandardException):
    """Exception raised if an attempt to modify project files occur"""
    pass

class InstanceNotFoundError(StandardException):
    """Exception is raised when 'search' cannot find an instance"""
    pass

class InvalidShapeError(StandardException):
    """Exception is raised when 'draw' receives an invalid shape"""
    pass

class CommandDoesNotExistError(StandardException):
    """Exception is raised when a command that does not exist is typed"""
    pass


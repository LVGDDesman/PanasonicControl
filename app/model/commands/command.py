#!/usr/bin/env python3
from functools import wraps

from .response import Response


def command_response(func):
    """
    Decorator to wrap execute methods
    """
    
    @wraps(func)
    def pack_into_response(*args, **kwargs) -> 'Response':
        """
        Executes the command and packs its result into a Response object.
        :raises SyntaxError: When wrong method was decorated
        """
        # Only methods named execute are allowed to be decorated
        if func.__name__ != "execute":
            raise SyntaxError(
                "Cannot decorate method called: {} ! Must be named: {} !".format(func.__name__, "execute"))

        try:
            # Wrap into responses when execution successful
            return Response(True, data=func(*args, **kwargs))
        except Exception as ex:
            # Some error occurred while executing command return error response
            return Response(False, error_message=str(ex))

    # Return the wrapper func
    return pack_into_response


class Command:
    """
    Inheritance Class for all executable commands
    """
    
    # raisable Errors:
    err_not_successful = Exception("Camera: Execution not sucessful")
    err_not_found = Exception("Camera: Not found") # probably not necessary
    err_file = Exception("Client: Can\'t save picture")
    err_param = ValueError("Client: Wrong Parameter")
    err_unknown = Exception("Error in Execution")
    # err_connection raised by request.get() -> ConnectionError("Connection not possible")


    @staticmethod
    @command_response
    def execute(*args, **kwargs):
        """
        execute-function, that should be implemented by every Child class.
        """
        raise NotImplementedError("Command itself shouldn't be able to be used")

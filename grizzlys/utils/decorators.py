from functools import wraps
from typing import Sequence

import juliacall

jl = juliacall.newmodule("grizzlys")


def julia_using_modules(modules: Sequence[str]):
    def using_decorator(function: callable):
        @wraps(function)
        def wrapper(*args, **kwargs):
            jl.seval(rf"using {','.join(modules)}")
            return function(*args, **kwargs)

        return wrapper

    return using_decorator

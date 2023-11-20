"""Array API dispatching implementation."""

from array_api.linalg import _core, _namespace
from array_api.linalg._core import *
from array_api.linalg._namespace import *

__all__ = []
__all__ += _core.__all__
__all__ += _namespace.__all__

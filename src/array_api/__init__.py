"""Array API."""


from array_api import (
    _array,
    _constants,
    _creation_functions,
    _data_type_functions,
    _device,
    _dtype,
    _elementwise_functions,
    _linear_algebra_functions,
    _manipulation_functions,
    _namespace,
    _namespace_api,
    _searching_functions,
    _set_functions,
    _sorting_functions,
    _statistical_functions,
    _types,
    _utility_functions,
)
from array_api._array import *
from array_api._constants import *
from array_api._creation_functions import *
from array_api._data_type_functions import *
from array_api._device import *
from array_api._dtype import *
from array_api._elementwise_functions import *
from array_api._linear_algebra_functions import *
from array_api._manipulation_functions import *
from array_api._namespace import *
from array_api._namespace_api import *
from array_api._searching_functions import *
from array_api._set_functions import *
from array_api._sorting_functions import *
from array_api._statistical_functions import *
from array_api._types import *
from array_api._utility_functions import *

__all__ = []
# From the Standard:
__all__ += _constants.__all__
__all__ += _types.__all__
# functions
__all__ += _creation_functions.__all__
__all__ += _data_type_functions.__all__
__all__ += _elementwise_functions.__all__
__all__ += _linear_algebra_functions.__all__
__all__ += _manipulation_functions.__all__
__all__ += _searching_functions.__all__
__all__ += _set_functions.__all__
__all__ += _sorting_functions.__all__
__all__ += _statistical_functions.__all__
__all__ += _utility_functions.__all__
# Additional types
__all__ += _array.__all__
__all__ += _device.__all__
__all__ += _dtype.__all__
__all__ += _namespace.__all__
__all__ += _namespace_api.__all__

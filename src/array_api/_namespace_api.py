"""Namespace utilities for array APIs."""

from __future__ import annotations

__all__ = ["ArrayAPINamespace"]

from typing import Protocol

from array_api._constants import HasConstants
from array_api._creation_functions import HasCreationFunctions
from array_api._data_type_functions import HasDataTypeFunctions
from array_api._elementwise_functions import HasElementwiseFunctions
from array_api._linear_algebra_functions import HasLinearAlgebraFunctions
from array_api._manipulation_functions import HasManipulationFunctions
from array_api._searching_functions import HasSearchingFunctions
from array_api._set_functions import HasSetFunctions
from array_api._sorting_functions import HasSortingFunctions
from array_api._statistical_functions import HasStatisticalFunctions
from array_api._utility_functions import HasUtilityFunctions


class ArrayAPINamespace(
    HasConstants,
    HasCreationFunctions,
    HasDataTypeFunctions,
    HasElementwiseFunctions,
    HasLinearAlgebraFunctions,
    HasManipulationFunctions,
    HasSearchingFunctions,
    HasSetFunctions,
    HasSortingFunctions,
    HasStatisticalFunctions,
    HasUtilityFunctions,
    Protocol,
):
    """Runtime checkable protocol for the Array API namespace."""

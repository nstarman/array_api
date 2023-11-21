"""Data type functions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final, Protocol

from array_api._namespace import get_namespace

if TYPE_CHECKING:
    from array_api._array import Array
    from array_api._dtype import DType
    from array_api._types import finfo_object, iinfo_object

__all__ = ["astype", "broadcast_arrays", "broadcast_to"]


_EMPTY_DICT: Final[dict[str, Any]] = {}


def astype(x: Array, dtype: DType, /, *, copy: bool = True) -> Array:
    """
    Copies an array to a specified data type irrespective of
    :ref:`type-promotion` rules.

    .. note::

        Casting floating-point ``NaN`` and ``infinity`` values to integral data
        types is not specified and is implementation-dependent.

    .. note::

        When casting a boolean input array to a numeric data type, a value of
        ``True`` must cast to a numeric value equal to ``1``, and a value of
        ``False`` must cast to a numeric value equal to ``0``.

        When casting a numeric input array to ``bool``, a value of ``0`` must
        cast to ``False``, and a non-zero value must cast to ``True``.

    Parameters
    ----------
    x: array
        array to cast.
    dtype: dtype
        desired data type.
    copy: bool
        specifies whether to copy an array when the specified ``dtype`` matches
        the data type of the input array ``x``. If ``True``, a newly allocated
        array must always be returned. If ``False`` and the specified ``dtype``
        matches the data type of the input array, the input array must be
        returned; otherwise, a newly allocated must be returned. Default:
        ``True``.

    Returns
    -------
    out: array
        an array having the specified data type. The returned array must have
        the same shape as ``x``.
    """
    return get_namespace(x).astype(x, dtype, copy=copy)


def broadcast_arrays(*arrays: Array) -> list[Array]:
    """
    Broadcasts one or more Arrays against one another.

    Parameters
    ----------
    arrays: array
        an arbitrary number of to-be broadcasted arrays.

    Returns
    -------
    out: List[array]
        a list of broadcasted arrays. Each array must have the same shape.
        Each array must have the same dtype as its corresponding input
        array.
    """
    return get_namespace(*arrays).broadcast_arrays(*arrays)


def broadcast_to(x: Array, /, shape: tuple[int, ...]) -> Array:
    """
    Broadcasts an array to a specified shape.

    Parameters
    ----------
    x: array
        array to broadcast.
    shape: Tuple[int, ...]
        array shape. Must be compatible with ``x`` (see
        :ref:`broadcasting`). If the array is incompatible with the
        specified shape, the function should raise an exception.

    Returns
    -------
    out: array
        an array having a specified shape. Must have the same data type as
        ``x``.
    """
    return get_namespace(x).broadcast_to(x, shape=shape)


###############################################################################


class HasDataTypeFunctions(Protocol):
    @staticmethod
    def astype(x: Array, dtype: DType, /, *, copy: bool = True) -> Array:
        ...

    @staticmethod
    def broadcast_arrays(*arrays: Array) -> list[Array]:
        ...

    @staticmethod
    def broadcast_to(x: Array, /, shape: tuple[int, ...]) -> Array:
        ...

    @staticmethod
    def can_cast(from_: DType | Array, to: DType, /) -> bool:
        ...

    @staticmethod
    def finfo(type: DType | Array, /) -> finfo_object:
        ...

    @staticmethod
    def iinfo(type: DType | Array, /) -> iinfo_object:
        ...

    @staticmethod
    def result_type(*arrays_and_dtypes: Array | DType) -> DType:
        ...

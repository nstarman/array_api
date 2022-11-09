from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Any, Final

# LOCAL
from array_api.namespace import get_namespace

if TYPE_CHECKING:
    # LOCAL
    from array_api._types import finfo_object, iinfo_object
    from array_api.array import ArrayAPIConformant
    from array_api.dtype import DTypeConformant

__all__: list[str] = []


_EMPTY_DICT: Final[dict[str, Any]] = {}


def astype(x: ArrayAPIConformant, dtype: DTypeConformant, /, *, copy: bool = True) -> ArrayAPIConformant:
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


def broadcast_arrays(*arrays: ArrayAPIConformant) -> list[ArrayAPIConformant]:
    """
    Broadcasts one or more ArrayAPIConformants against one another.

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


def broadcast_to(x: ArrayAPIConformant, /, shape: tuple[int, ...]) -> ArrayAPIConformant:
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


def can_cast(from_: DTypeConformant | ArrayAPIConformant, to: DTypeConformant, /) -> bool:
    """
    Determines if one data type can be cast to another data type according
    :ref:`type-promotion` rules.

    Parameters
    ----------
    from_: Union[dtype, array]
        input data type or array from which to cast.
    to: dtype
        desired data type.

    Returns
    -------
    out: bool
        ``True`` if the cast can occur according to :ref:`type-promotion`
        rules; otherwise, ``False``.
    """
    try:
        xp = get_namespace(type)
    except ValueError as e:
        raise NotImplementedError("this function does not have a pre-determined output type") from e
    return xp.can_cast(from_, to)


def finfo(type: DTypeConformant | ArrayAPIConformant, /) -> finfo_object:
    """
    Machine limits for floating-point data types.

    Parameters
    ----------
    type: Union[dtype, array]
        the kind of floating-point data-type about which to get information.

    Returns
    -------
    out: finfo object
        an object having the following attributes:

        - **bits**: *int*

        number of bits occupied by the floating-point data type.

        - **eps**: *float*

        difference between 1.0 and the next smallest representable
        floating-point number larger than 1.0 according to the IEEE-754
        standard.

        - **max**: *float*

        largest representable number.

        - **min**: *float*

        smallest representable number.

        - **smallest_normal**: *float*

        smallest positive floating-point number with full precision.
    """
    try:
        xp = get_namespace(type)
    except ValueError as e:
        raise NotImplementedError("this function does not have a pre-determined output type") from e
    return xp.finfo(type)


def iinfo(type: DTypeConformant | ArrayAPIConformant, /) -> iinfo_object:
    """
    Machine limits for integer data types.

    Parameters
    ----------
    type: Union[dtype, array]
        the kind of integer data-type about which to get information.

    Returns
    -------
    out: iinfo object
        @mypyca
        class with that encapsules the following attributes:

        - **bits**: *int*

        number of bits occupied by the type.

        - **max**: *int*

        largest representable number.

        - **min**: *int*

        smallest representable number.
    """
    try:
        xp = get_namespace(type)
    except ValueError as e:
        raise NotImplementedError("this function does not have a pre-determined output type") from e
    return xp.iinfo(type)


def result_type(*arrays_and_dtypes: ArrayAPIConformant | DTypeConformant) -> DTypeConformant:
    """
    Returns the dtype that results from applying the type promotion rules (see
    :ref:`type-promotion`) to the arguments.

    .. note::

        If provided mixed dtypes (e.g., integer and floating-point), the
        returned dtype will be implementation-specific.

    Parameters
    ----------
    arrays_and_dtypes: Union[array, dtype]
        an arbitrary number of input arrays and/or dtypes.

    Returns
    -------
    out: dtype
        the dtype resulting from an operation involving the input arrays and
        dtypes.
    """
    try:
        xp = get_namespace(*arrays_and_dtypes)
    except ValueError as e:
        raise NotImplementedError("this function does not have a pre-determined output type") from e
    return xp.result_type(*arrays_and_dtypes)

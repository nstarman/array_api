from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Any, Final

# LOCAL
from array_api.namespace import get_namespace

if TYPE_CHECKING:
    # LOCAL
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

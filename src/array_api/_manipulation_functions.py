"""Manipulation functions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from array_api._namespace import get_namespace

if TYPE_CHECKING:
    from array_api._array import Array
    from array_api._types import AxisT

__all__ = [
    "concat",
    "expand_dims",
    "flip",
    "permute_dims",
    "reshape",
    "roll",
    "squeeze",
    "stack",
]


def concat(
    arrays: tuple[Array, ...] | list[Array],
    /,
    *,
    axis: int | None = 0,
) -> Array:
    """
    Joins a sequence of arrays along an existing axis.

    Parameters
    ----------
    arrays: Union[Tuple[array, ...], List[array]]
        input arrays to join. The arrays must have the same shape, except in the
        dimension specified by ``axis``.
    axis: Optional[int]
        axis along which the arrays will be joined. If ``axis`` is ``None``,
        arrays must be flattened before concatenation. If ``axis`` is negative,
        the function must determine the axis along which to join by counting
        from the last dimension. Default: ``0``.

    Returns
    -------
    out: array
        an output array containing the concatenated values. If the input arrays
        have different data types, normal :ref:`type-promotion` must apply. If
        the input arrays have the same data type, the output array must have the
        same data type as the input arrays.

        .. note::

            This specification leaves type promotion between data type families
            (i.e., ``intxx`` and ``floatxx``) unspecified.
    """
    return get_namespace(*arrays).concat(arrays, axis=axis)


def expand_dims(x: Array, /, *, axis: int = 0) -> Array:
    """
    Expands the shape of an array by inserting a new axis (dimension) of size
    one at the position specified by ``axis``.

    Parameters
    ----------
    x: array
        input array.
    axis: int
        axis position (zero-based). If ``x`` has rank (i.e, number of
        dimensions) ``N``, a valid ``axis`` must reside on the closed-interval
        ``[-N-1, N]``. If provided a negative ``axis``, the axis position at
        which to insert a singleton dimension must be computed as ``N + axis +
        1``. Hence, if provided ``-1``, the resolved axis position must be ``N``
        (i.e., a singleton dimension must be appended to the input array ``x``).
        If provided ``-N-1``, the resolved axis position must be ``0`` (i.e., a
        singleton dimension must be prepended to the input array ``x``). An
        ``IndexError`` exception must be raised if provided an invalid ``axis``
        position.

    Returns
    -------
    out: array
        an expanded output array having the same data type as ``x``.
    """
    return get_namespace(x).expand_dims(x, axis=axis)


def flip(x: Array, /, *, axis: AxisT = None) -> Array:
    """
    Reverses the order of elements in an array along the given axis. The shape
    of the array must be preserved.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[int | tuple[int, ...]]
        axis (or axes) along which to flip. If ``axis`` is ``None``, the
        function must flip all input array axes. If ``axis`` is negative, the
        function must count from the last dimension. If provided more than one
        axis, the function must flip only the specified axes. Default: ``None``.

    Returns
    -------
    out: array
        an output array having the same data type and shape as ``x`` and whose
        elements, relative to ``x``, are reordered.
    """
    return get_namespace(x).flip(x, axis=axis)


def permute_dims(x: Array, /, axes: tuple[int, ...]) -> Array:
    """
    Permutes the axes (dimensions) of an array ``x``.

    Parameters
    ----------
    x: array
        input array.
    axes: Tuple[int, ...]
        tuple containing a permutation of ``(0, 1, ..., N-1)`` where ``N`` is
        the number of axes (dimensions) of ``x``.

    Returns
    -------
    out: array
        an array containing the axes permutation. The returned array must have
        the same data type as ``x``.
    """
    return get_namespace(x).permute_dims(x, axes=axes)


def reshape(
    x: Array,
    /,
    shape: tuple[int, ...],
    *,
    copy: bool | None = None,
) -> Array:
    """
    Reshapes an array without changing its data.

    Parameters
    ----------
    x: array
        input array to reshape.
    shape: Tuple[int, ...]
        a new shape compatible with the original shape. One shape dimension is
        allowed to be ``-1``. When a shape dimension is ``-1``, the
        corresponding output array shape dimension must be inferred from the
        length of the array and the remaining dimensions.
    copy: Optional[bool]
        boolean indicating whether or not to copy the input array. If ``True``,
        the function must always copy. If ``False``, the function must never
        copy and must raise a ``ValueError`` in case a copy would be necessary.
        If ``None``, the function must reuse existing memory buffer if possible
        and copy otherwise. Default: ``None``.

    Returns
    -------
    out: array
        an output array having the same data type and elements as ``x``.
    """
    return get_namespace(x).reshape(x, shape=shape, copy=copy)


def roll(
    x: Array, /, shift: int | tuple[int, ...], *, axis: AxisT = None
) -> Array:
    """
    Rolls array elements along a specified axis. Array elements that roll beyond
    the last position are re-introduced at the first position. Array elements
    that roll beyond the first position are re-introduced at the last position.

    Parameters
    ----------
    x: array
        input array.
    shift: int | tuple[int, ...]
        number of places by which the elements are shifted. If ``shift`` is a
        tuple, then ``axis`` must be a tuple of the same size, and each of the
        given axes must be shifted by the corresponding element in ``shift``. If
        ``shift`` is an ``int`` and ``axis`` a tuple, then the same ``shift``
        must be used for all specified axes. If a shift is positive, then array
        elements must be shifted positively (toward larger indices) along the
        dimension of ``axis``. If a shift is negative, then array elements must
        be shifted negatively (toward smaller indices) along the dimension of
        ``axis``.
    axis: Optional[int | tuple[int, ...]]
        axis (or axes) along which elements to shift. If ``axis`` is ``None``,
        the array must be flattened, shifted, and then restored to its original
        shape. Default: ``None``.

    Returns
    -------
    out: array
        an output array having the same data type as ``x`` and whose elements,
        relative to ``x``, are shifted.
    """
    return get_namespace(x).roll(x, shift=shift, axis=axis)


def squeeze(x: Array, /, axis: int | tuple[int, ...]) -> Array:
    """
    Removes singleton dimensions (axes) from ``x``.

    Parameters
    ----------
    x: array
        input array.
    axis: int | tuple[int, ...]
        axis (or axes) to squeeze. If a specified axis has a size greater than
        one, a ``ValueError`` must be raised.

    Returns
    -------
    out: array
        an output array having the same data type and elements as ``x``.
    """
    return get_namespace(x).squeeze(x, axis=axis)


def stack(
    arrays: tuple[Array, ...] | list[Array],
    /,
    *,
    axis: int = 0,
) -> Array:
    """
    Joins a sequence of arrays along a new axis.

    Parameters
    ----------
    arrays: Union[Tuple[array, ...], List[array]]
        input arrays to join. Each array must have the same shape.
    axis: int
        axis along which the arrays will be joined. Providing an ``axis``
        specifies the index of the new axis in the dimensions of the result. For
        example, if ``axis`` is ``0``, the new axis will be the first dimension
        and the output array will have shape ``(N, A, B, C)``; if ``axis`` is
        ``1``, the new axis will be the second dimension and the output array
        will have shape ``(A, N, B, C)``; and, if ``axis`` is ``-1``, the new
        axis will be the last dimension and the output array will have shape
        ``(A, B, C, N)``. A valid ``axis`` must be on the interval ``[-N, N)``,
        where ``N`` is the rank (number of dimensions) of ``x``. If provided an
        ``axis`` outside of the required interval, the function must raise an
        exception. Default: ``0``.

    Returns
    -------
    out: array
        an output array having rank ``N+1``, where ``N`` is the rank (number of
        dimensions) of ``x``. If the input arrays have different data types,
        normal :ref:`type-promotion` must apply. If the input arrays have the
        same data type, the output array must have the same data type as the
        input arrays.

        .. note::

            This specification leaves type promotion between data type families
            (i.e., ``intxx`` and ``floatxx``) unspecified.
    """
    return get_namespace(*arrays).stack(arrays, axis=axis)

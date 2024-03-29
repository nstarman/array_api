"""Sorting functions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from array_api._namespace import get_namespace

if TYPE_CHECKING:
    from array_api._array import Array
    from array_api._types import AxisT

__all__ = ["all", "any"]


def all(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
) -> Array:
    """
    Tests whether all input array elements evaluate to ``True`` along a
    specified axis.

    .. note::

        Positive infinity, negative infinity, and NaN must evaluate to ``True``.

    .. note::

        If ``x`` is an empty array or the size of the axis (dimension) along
        which to evaluate elements is zero, the test result must be ``True``.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[int | tuple[int, ...]]
        axis or axes along which to perform a logical AND reduction. By default,
        a logical AND reduction must be performed over the entire array. If a
        tuple of integers, logical AND reductions must be performed over
        multiple axes. A valid ``axis`` must be an integer on the interval
        ``[-N, N)``, where ``N`` is the rank (number of dimensions) of ``x``. If
        an ``axis`` is specified as a negative integer, the function must
        determine the axis along which to perform a reduction by counting
        backward from the last dimension (where ``-1`` refers to the last
        dimension). If provided an invalid ``axis``, the function must raise an
        exception. Default: ``None``.
    keepdims: bool
        If ``True``, the reduced axes (dimensions) must be included in the
        result as singleton dimensions, and, accordingly, the result must be
        compatible with the input array (see :ref:`broadcasting`). Otherwise, if
        ``False``, the reduced axes (dimensions) must not be included in the
        result. Default: ``False``.

    Returns
    -------
    out: array
        if a logical AND reduction was performed over the entire array, the
        returned array must be a zero-dimensional array containing the test
        result; otherwise, the returned array must be a non-zero-dimensional
        array containing the test results. The returned array must have a data
        type of ``bool``.

    """
    return get_namespace(x).all(x, axis=axis, keepdims=keepdims)


def any(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
) -> Array:
    """
    Tests whether any input array element evaluates to ``True`` along a
    specified axis.

    .. note::

        Positive infinity, negative infinity, and NaN must evaluate to ``True``.

    .. note::

        If ``x`` is an empty array or the size of the axis (dimension) along
        which to evaluate elements is zero, the test result must be ``False``.

    Parameters
    ----------
    x: array
        input array.
    axis: Optional[int | tuple[int, ...]]
        axis or axes along which to perform a logical OR reduction. By default,
        a logical OR reduction must be performed over the entire array. If a
        tuple of integers, logical OR reductions must be performed over multiple
        axes. A valid ``axis`` must be an integer on the interval ``[-N, N)``,
        where ``N`` is the rank (number of dimensions) of ``x``. If an ``axis``
        is specified as a negative integer, the function must determine the axis
        along which to perform a reduction by counting backward from the last
        dimension (where ``-1`` refers to the last dimension). If provided an
        invalid ``axis``, the function must raise an exception. Default:
        ``None``.
    keepdims: bool
        If ``True``, the reduced axes (dimensions) must be included in the
        result as singleton dimensions, and, accordingly, the result must be
        compatible with the input array (see :ref:`broadcasting`). Otherwise, if
        ``False``, the reduced axes (dimensions) must not be included in the
        result. Default: ``False``.

    Returns
    -------
    out: array
        if a logical OR reduction was performed over the entire array, the
        returned array must be a zero-dimensional array containing the test
        result; otherwise, the returned array must be a non-zero-dimensional
        array containing the test results. The returned array must have a data
        type of ``bool``.

    """
    return get_namespace(x).any(x, axis=axis, keepdims=keepdims)


####################################################################################################


class HasUtilityFunctions(Protocol):
    @staticmethod
    def all(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array: ...

    @staticmethod
    def any(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array: ...

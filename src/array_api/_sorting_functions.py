"""Sorting functions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from array_api._namespace import get_namespace

if TYPE_CHECKING:
    from array_api._array import Array

__all__ = ["sort", "argsort"]


def argsort(
    x: Array,
    /,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
) -> Array:
    """
    Returns the indices that sort an array ``x`` along a specified axis.

    Parameters
    ----------
    x : array
        input array.
    axis: int
        axis along which to sort. If set to ``-1``, the function must sort along
        the last axis. Default: ``-1``.
    descending: bool
        sort order. If ``True``, the returned indices sort ``x`` in descending
        order (by value). If ``False``, the returned indices sort ``x`` in
        ascending order (by value). Default: ``False``.
    stable: bool
        sort stability. If ``True``, the returned indices must maintain the
        relative order of ``x`` values which compare as equal. If ``False``, the
        returned indices may or may not maintain the relative order of ``x``
        values which compare as equal (i.e., the relative order of ``x`` values
        which compare as equal is implementation-dependent). Default: ``True``.

    Returns
    -------
    out : array
        an array of indices. The returned array must have the same shape as
        ``x``. The returned array must have the default array index data type.

    """
    return get_namespace(x).argsort(
        x, axis=axis, descending=descending, stable=stable
    )


def sort(
    x: Array,
    /,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
) -> Array:
    """
    Returns a sorted copy of an input array ``x``.

    Parameters
    ----------
    x: array
        input array.
    axis: int
        axis along which to sort. If set to ``-1``, the function must sort along
        the last axis. Default: ``-1``.
    descending: bool
        sort order. If ``True``, the array must be sorted in descending order
        (by value). If ``False``, the array must be sorted in ascending order
        (by value). Default: ``False``.
    stable: bool
        sort stability. If ``True``, the returned array must maintain the
        relative order of ``x`` values which compare as equal. If ``False``, the
        returned array may or may not maintain the relative order of ``x``
        values which compare as equal (i.e., the relative order of ``x`` values
        which compare as equal is implementation-dependent). Default: ``True``.

    Returns
    -------
    out : array
        a sorted array. The returned array must have the same data type and
        shape as ``x``.

    """
    return get_namespace(x).sort(
        x, axis=axis, descending=descending, stable=stable
    )


####################################################################################################


class HasSortingFunctions(Protocol):
    @staticmethod
    def argsort(
        x: Array,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> Array: ...

    @staticmethod
    def sort(
        x: Array,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> Array: ...

"""DType protocol."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

__all__ = ["DType"]


@runtime_checkable
class DType(Protocol):
    """Runtime-checkable protocol for the dtype."""

    def __eq__(self: DType, other: DType, /) -> bool:
        """
        Computes the truth value of ``self == other`` in order to test for data
        type object equality.

        Parameters
        ----------
        self: dtype
            data type instance. May be any supported data type.
        other: dtype
            other data type instance. May be any supported data type.

        Returns
        -------
        out: bool
            a boolean indicating whether the data type objects are equal.
        """
        ...

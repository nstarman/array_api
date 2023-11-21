"""
Types for annotations.

The type variables should be replaced with the actual types for a given
library, e.g., for NumPy TypeVar('array') would be replaced with ndarray.
"""
from __future__ import annotations

__all__ = [
    "PyCapsule",
    "SupportsBufferProtocol",
    "finfo_object",
    "iinfo_object",
]

from typing import Any, Protocol, TypeVar

SupportsBufferProtocol = Any
PyCapsule = Any
_T_co = TypeVar("_T_co", covariant=True)
AxisT = int | tuple[int, ...] | None


class finfo_object(Protocol):  # noqa: N801
    """object returned by finfo."""

    bits: int
    eps: float
    max: float
    min: float
    smallest_normal: float


class iinfo_object(Protocol):  # noqa: N801
    """object returned by iinfo."""

    bits: int
    max: int
    min: int


class NestedSequence(Protocol[_T_co]):
    """Nested sequence."""

    def __getitem__(self, key: int, /) -> _T_co | NestedSequence[_T_co]:
        ...

    def __len__(self, /) -> int:
        ...

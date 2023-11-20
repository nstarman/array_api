"""Namespace utilities for array APIs."""

from __future__ import annotations

__all__ = ["get_namespace", "ArrayAPINamespace"]

from typing import TYPE_CHECKING, Any, Protocol

from array_api._array import Array

if TYPE_CHECKING:
    from collections.abc import Sequence

    from array_api._device import Device
    from array_api._dtype import DType
    from array_api._types import (
        AxisT,
        NestedSequence,
        SupportsBufferProtocol,
        finfo_object,
        iinfo_object,
    )
    from array_api.linalg import ArrayAPILinAlgNamespace


def get_namespace(
    *xs: Any,  # noqa: ANN401
    array_traits: type | tuple[type, ...] = Array,
    api_version: str | None = None,
) -> ArrayAPINamespace:
    """
    Get the array API namespace for the given array inputs.

    Parameters
    ----------
    *xs : Any
        Input arrays for which to get the array API namespace.
    array_traits : type | tuple[type, ...], optional
        The array traits to check for, by default full `Array`.  If a tuple,
        this checks for ALL of the traits (formally this is an intersection of
        the traits). For example, if `array_traits` is ``(Array, Mapping)``,
        then the inputs must be both ``Array`` and ``Mapping`` to be considered
        conformant.
    api_version : str | None, optional
        The array API version, by default `None`.

    Returns
    -------
    `~array_api._types.ArrayAPINamespace`
        The array API namespace for the given array inputs.

    Raises
    ------
    ValueError
        If none of the inputs are array API conformant.  If the inputs are from
        multiple array API namespaces.
    """
    # `xs` contains one or more arrays.
    namespaces: set[ArrayAPINamespace] = {
        x.__array_namespace__(api_version=api_version)
        for x in xs
        if all(
            isinstance(x, trait)
            for trait in (
                array_traits
                if isinstance(array_traits, tuple)
                else (array_traits,)
            )
        )
    }

    if not namespaces:
        msg = "Unrecognized array input"
        raise ValueError(msg)
    if len(namespaces) != 1:
        msg = f"Multiple namespaces for array inputs: {namespaces}"
        raise ValueError(msg)

    return namespaces.pop()


####################################################################################################


class ArrayAPINamespace(Protocol):
    """Runtime checkable protocol for the Array API namespace."""

    # ===============================================================
    # Constants

    @property
    def e(self) -> float:
        ...

    @property
    def inf(self) -> float:
        ...

    @property
    def nan(self) -> float:
        ...

    @property
    def newaxis(self) -> float:
        ...

    @property
    def pi(self) -> float:
        ...

    # ===============================================================
    # Creation Functions

    @staticmethod
    def arange(
        start: float,
        /,
        stop: float | None = None,
        step: float = 1,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def asarray(
        obj: Array
        | bool
        | float
        | NestedSequence[bool | float]
        | SupportsBufferProtocol,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
        copy: bool | None = None,
    ) -> Array:
        ...

    @staticmethod
    def empty_like(
        x: Array, /, *, dtype: DType | None = None, device: Device | None = None
    ) -> Array:
        ...

    @staticmethod
    def eye(
        n_rows: int,
        n_cols: int | None = None,
        /,
        *,
        k: int = 0,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def from_dlpack(x: object, /) -> Array:
        ...

    @staticmethod
    def full(
        shape: int | tuple[int, ...],
        fill_value: float,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def full_like(
        x: Array,
        /,
        fill_value: float,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def linspace(
        start: float,
        stop: float,
        /,
        num: int,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
        endpoint: bool = True,
    ) -> Array:
        ...

    @staticmethod
    def meshgrid(*arrays: Array, indexing: str = "xy") -> list[Array]:
        ...

    @staticmethod
    def ones(
        shape: int | tuple[int, ...],
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def ones_like(
        x: Array,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def tril(x: Array, /, *, k: int = 0) -> Array:
        ...

    @staticmethod
    def triu(x: Array, /, *, k: int = 0) -> Array:
        ...

    @staticmethod
    def zeros(
        shape: int | tuple[int, ...],
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> Array:
        ...

    @staticmethod
    def zeros_like(
        x: Array, /, *, dtype: DType | None = None, device: Device | None = None
    ) -> Array:
        ...

    # ===============================================================
    # Data Type Functions

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

    # ===============================================================
    # Elementwise Functions

    @staticmethod
    def abs(x: Array, /) -> Array:
        ...

    @staticmethod
    def acos(x: Array, /) -> Array:
        ...

    @staticmethod
    def acosh(x: Array, /) -> Array:
        ...

    @staticmethod
    def add(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def asin(x: Array, /) -> Array:
        ...

    @staticmethod
    def asinh(x: Array, /) -> Array:
        ...

    @staticmethod
    def atan(x: Array, /) -> Array:
        ...

    @staticmethod
    def atan2(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def atanh(x: Array, /) -> Array:
        ...

    @staticmethod
    def bitwise_and(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def bitwise_left_shift(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def bitwise_invert(x: Array, /) -> Array:
        ...

    @staticmethod
    def bitwise_or(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def bitwise_right_shift(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def bitwise_xor(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def ceil(x: Array, /) -> Array:
        ...

    @staticmethod
    def cos(x: Array, /) -> Array:
        ...

    @staticmethod
    def cosh(x: Array, /) -> Array:
        ...

    @staticmethod
    def divide(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def equal(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def exp(x: Array, /) -> Array:
        ...

    @staticmethod
    def expm1(x: Array, /) -> Array:
        ...

    @staticmethod
    def floor(x: Array, /) -> Array:
        ...

    @staticmethod
    def floor_divide(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def greater(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def greater_equal(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def isfinite(x: Array, /) -> Array:
        ...

    @staticmethod
    def isinf(x: Array, /) -> Array:
        ...

    @staticmethod
    def isnan(x: Array, /) -> Array:
        ...

    @staticmethod
    def less(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def less_equal(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def log(x: Array, /) -> Array:
        ...

    @staticmethod
    def log1p(x: Array, /) -> Array:
        ...

    @staticmethod
    def log2(x: Array, /) -> Array:
        ...

    @staticmethod
    def log10(x: Array, /) -> Array:
        ...

    @staticmethod
    def logaddexp(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def logical_and(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def logical_not(x: Array, /) -> Array:
        ...

    @staticmethod
    def logical_or(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def logical_xor(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def multiply(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def negative(x: Array, /) -> Array:
        ...

    @staticmethod
    def not_equal(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def positive(x: Array, /) -> Array:
        ...

    @staticmethod
    def pow(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def remainder(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def round(x: Array, /) -> Array:
        ...

    @staticmethod
    def sign(x: Array, /) -> Array:
        ...

    @staticmethod
    def sin(x: Array, /) -> Array:
        ...

    @staticmethod
    def sinh(x: Array, /) -> Array:
        ...

    @staticmethod
    def square(x: Array, /) -> Array:
        ...

    @staticmethod
    def sqrt(x: Array, /) -> Array:
        ...

    @staticmethod
    def subtract(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def tan(x: Array, /) -> Array:
        ...

    @staticmethod
    def tanh(x: Array, /) -> Array:
        ...

    @staticmethod
    def trunc(x: Array, /) -> Array:
        ...

    # ===============================================================
    # Linalg

    @property
    def linalg(self) -> ArrayAPILinAlgNamespace:
        ...

    @staticmethod
    def matmul(x1: Array, x2: Array, /) -> Array:
        ...

    @staticmethod
    def matrix_transpose(x: Array, /) -> Array:
        ...

    @staticmethod
    def tensordot(
        x1: Array,
        x2: Array,
        /,
        *,
        axes: int | tuple[Sequence[int], Sequence[int]] = 2,
    ) -> Array:
        ...

    @staticmethod
    def vecdot(x1: Array, x2: Array, /, *, axis: int = -1) -> Array:
        ...

    # ===============================================================
    # Manipulation

    @staticmethod
    def concat(
        arrays: tuple[Array, ...] | list[Array], /, *, axis: int | None = 0
    ) -> Array:
        ...

    @staticmethod
    def expand_dims(x: Array, /, *, axis: int = 0) -> Array:
        ...

    @staticmethod
    def flip(x: Array, /, *, axis: AxisT = None) -> Array:
        ...

    @staticmethod
    def permute_dims(x: Array, /, axes: tuple[int, ...]) -> Array:
        ...

    @staticmethod
    def reshape(
        x: Array, /, shape: tuple[int, ...], *, copy: bool | None = None
    ) -> Array:
        ...

    @staticmethod
    def roll(
        x: Array,
        /,
        shift: int | tuple[int, ...],
        *,
        axis: AxisT = None,
    ) -> Array:
        ...

    @staticmethod
    def squeeze(x: Array, /, axis: int | tuple[int, ...]) -> Array:
        ...

    @staticmethod
    def stack(
        arrays: tuple[Array, ...] | list[Array], /, *, axis: int = 0
    ) -> Array:
        ...

    # ===============================================================
    # Searching

    @staticmethod
    def argmax(
        x: Array, /, *, axis: int | None = None, keepdims: bool = False
    ) -> Array:
        ...

    @staticmethod
    def argmin(
        x: Array, /, *, axis: int | None = None, keepdims: bool = False
    ) -> Array:
        ...

    @staticmethod
    def nonzero(x: Array, /) -> tuple[Array, ...]:
        ...

    @staticmethod
    def where(condition: Array, x1: Array, x2: Array, /) -> Array:
        ...

    # ===============================================================
    # Set

    @staticmethod
    def unique_all(x: Array, /) -> tuple[Array, Array, Array, Array]:
        ...

    @staticmethod
    def unique_counts(x: Array, /) -> tuple[Array, Array]:
        ...

    @staticmethod
    def unique_inverse(x: Array, /) -> tuple[Array, Array]:
        ...

    @staticmethod
    def unique_values(x: Array, /) -> Array:
        ...

    # ===============================================================
    # Sort

    @staticmethod
    def argsort(
        x: Array,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> Array:
        ...

    @staticmethod
    def sort(
        x: Array,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> Array:
        ...

    # ===============================================================
    # Statistical

    @staticmethod
    def max(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def mean(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def min(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def prod(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        dtype: DType | None = None,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def std(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        correction: float = 0.0,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def sum(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        dtype: DType | None = None,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def var(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        correction: float = 0.0,
        keepdims: bool = False,
    ) -> Array:
        ...

    # ===============================================================
    # Utility

    @staticmethod
    def all(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array:
        ...

    @staticmethod
    def any(
        x: Array,
        /,
        *,
        axis: AxisT = None,
        keepdims: bool = False,
    ) -> Array:
        ...

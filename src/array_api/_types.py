"""
Types for annotations.

The type variables should be replaced with the actual types for a given
library, e.g., for NumPy TypeVar('array') would be replaced with ndarray.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol, TypeVar

if TYPE_CHECKING:
    from collections.abc import Sequence

    from array_api.array import ArrayAPI
    from array_api.device import Device
    from array_api.dtype import DType
    from array_api.linalg._types import ArrayAPILinAlgNamespace

SupportsBufferProtocol = Any
PyCapsule = Any
_T_co = TypeVar("_T_co", covariant=True)


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
        start: int | float,
        /,
        stop: int | float | None = None,
        step: int | float = 1,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def asarray(
        obj: ArrayAPI
        | bool
        | int
        | float
        | NestedSequence[bool | int | float]
        | SupportsBufferProtocol,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
        copy: bool | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def empty_like(
        x: ArrayAPI,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
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
    ) -> ArrayAPI:
        ...

    @staticmethod
    def from_dlpack(x: object, /) -> ArrayAPI:
        ...

    @staticmethod
    def full(
        shape: int | tuple[int, ...],
        fill_value: int | float,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def full_like(
        x: ArrayAPI,
        /,
        fill_value: int | float,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def linspace(
        start: int | float,
        stop: int | float,
        /,
        num: int,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
        endpoint: bool = True,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def meshgrid(*arrays: ArrayAPI, indexing: str = "xy") -> list[ArrayAPI]:
        ...

    @staticmethod
    def ones(
        shape: int | tuple[int, ...],
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def ones_like(
        x: ArrayAPI,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def tril(x: ArrayAPI, /, *, k: int = 0) -> ArrayAPI:
        ...

    @staticmethod
    def triu(x: ArrayAPI, /, *, k: int = 0) -> ArrayAPI:
        ...

    @staticmethod
    def zeros(
        shape: int | tuple[int, ...],
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def zeros_like(
        x: ArrayAPI,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
    ) -> ArrayAPI:
        ...

    # ===============================================================
    # Data Type Functions

    @staticmethod
    def astype(x: ArrayAPI, dtype: DType, /, *, copy: bool = True) -> ArrayAPI:
        ...

    @staticmethod
    def broadcast_arrays(*arrays: ArrayAPI) -> list[ArrayAPI]:
        ...

    @staticmethod
    def broadcast_to(x: ArrayAPI, /, shape: tuple[int, ...]) -> ArrayAPI:
        ...

    @staticmethod
    def can_cast(from_: DType | ArrayAPI, to: DType, /) -> bool:
        ...

    @staticmethod
    def finfo(type: DType | ArrayAPI, /) -> finfo_object:
        ...

    @staticmethod
    def iinfo(type: DType | ArrayAPI, /) -> iinfo_object:
        ...

    @staticmethod
    def result_type(*arrays_and_dtypes: ArrayAPI | DType) -> DType:
        ...

    # ===============================================================
    # Elementwise Functions

    @staticmethod
    def abs(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def acos(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def acosh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def add(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def asin(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def asinh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def atan(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def atan2(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def atanh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def bitwise_and(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def bitwise_left_shift(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def bitwise_invert(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def bitwise_or(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def bitwise_right_shift(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def bitwise_xor(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def ceil(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def cos(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def cosh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def divide(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def equal(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def exp(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def expm1(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def floor(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def floor_divide(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def greater(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def greater_equal(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def isfinite(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def isinf(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def isnan(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def less(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def less_equal(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def log(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def log1p(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def log2(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def log10(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def logaddexp(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def logical_and(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def logical_not(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def logical_or(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def logical_xor(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def multiply(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def negative(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def not_equal(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def positive(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def pow(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def remainder(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def round(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def sign(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def sin(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def sinh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def square(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def sqrt(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def subtract(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def tan(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def tanh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def trunc(x: ArrayAPI, /) -> ArrayAPI:
        ...

    # ===============================================================
    # Linalg

    @property
    def linalg(self) -> ArrayAPILinAlgNamespace:
        ...

    @staticmethod
    def matmul(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def matrix_transpose(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def tensordot(
        x1: ArrayAPI,
        x2: ArrayAPI,
        /,
        *,
        axes: int | tuple[Sequence[int], Sequence[int]] = 2,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def vecdot(x1: ArrayAPI, x2: ArrayAPI, /, *, axis: int = -1) -> ArrayAPI:
        ...

    # ===============================================================
    # Manipulation

    @staticmethod
    def concat(
        arrays: tuple[ArrayAPI, ...] | list[ArrayAPI],
        /,
        *,
        axis: int | None = 0,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def expand_dims(x: ArrayAPI, /, *, axis: int = 0) -> ArrayAPI:
        ...

    @staticmethod
    def flip(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def permute_dims(x: ArrayAPI, /, axes: tuple[int, ...]) -> ArrayAPI:
        ...

    @staticmethod
    def reshape(
        x: ArrayAPI,
        /,
        shape: tuple[int, ...],
        *,
        copy: bool | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def roll(
        x: ArrayAPI,
        /,
        shift: int | tuple[int, ...],
        *,
        axis: int | tuple[int, ...] | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def squeeze(x: ArrayAPI, /, axis: int | tuple[int, ...]) -> ArrayAPI:
        ...

    @staticmethod
    def stack(
        arrays: tuple[ArrayAPI, ...] | list[ArrayAPI],
        /,
        *,
        axis: int = 0,
    ) -> ArrayAPI:
        ...

    # ===============================================================
    # Searching

    @staticmethod
    def argmax(
        x: ArrayAPI,
        /,
        *,
        axis: int | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def argmin(
        x: ArrayAPI,
        /,
        *,
        axis: int | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def nonzero(x: ArrayAPI, /) -> tuple[ArrayAPI, ...]:
        ...

    @staticmethod
    def where(condition: ArrayAPI, x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    # ===============================================================
    # Set

    @staticmethod
    def unique_all(
        x: ArrayAPI,
        /,
    ) -> tuple[ArrayAPI, ArrayAPI, ArrayAPI, ArrayAPI]:
        ...

    @staticmethod
    def unique_counts(x: ArrayAPI, /) -> tuple[ArrayAPI, ArrayAPI]:
        ...

    @staticmethod
    def unique_inverse(x: ArrayAPI, /) -> tuple[ArrayAPI, ArrayAPI]:
        ...

    @staticmethod
    def unique_values(x: ArrayAPI, /) -> ArrayAPI:
        ...

    # ===============================================================
    # Sort

    @staticmethod
    def argsort(
        x: ArrayAPI,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def sort(
        x: ArrayAPI,
        /,
        *,
        axis: int = -1,
        descending: bool = False,
        stable: bool = True,
    ) -> ArrayAPI:
        ...

    # ===============================================================
    # Statistical

    @staticmethod
    def max(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def mean(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def min(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def prod(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        dtype: DType | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def std(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        correction: int | float = 0.0,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def sum(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        dtype: DType | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def var(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        correction: int | float = 0.0,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    # ===============================================================
    # Utility

    @staticmethod
    def all(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def any(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
    ) -> ArrayAPI:
        ...

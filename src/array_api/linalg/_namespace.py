from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

if TYPE_CHECKING:
    from collections.abc import Sequence

    from array_api._array import Array

__all__ = ["ArrayAPILinAlgNamespace"]


class ArrayAPILinAlgNamespace(Protocol):
    """Runtime-checkable protocol for linear algebra namespace."""

    @staticmethod
    def cholesky(x: Array, /, *, upper: bool = False) -> Array: ...

    @staticmethod
    def cross(x1: Array, x2: Array, /, *, axis: int = -1) -> Array: ...

    @staticmethod
    def det(x: Array, /) -> Array: ...

    @staticmethod
    def diagonal(x: Array, /, *, offset: int = 0) -> Array: ...

    @staticmethod
    def eigh(x: Array, /) -> tuple[Array]: ...

    @staticmethod
    def eigvalsh(x: Array, /) -> Array: ...

    @staticmethod
    def inv(x: Array, /) -> Array: ...

    @staticmethod
    def matmul(x1: Array, x2: Array, /) -> Array: ...

    @staticmethod
    def matrix_norm(
        x: Array,
        /,
        *,
        keepdims: bool = False,
        ord: float | Literal["fro", "nuc"] | None = "fro",
    ) -> Array: ...

    @staticmethod
    def matrix_power(x: Array, n: int, /) -> Array: ...

    @staticmethod
    def matrix_rank(
        x: Array, /, *, rtol: float | Array | None = None
    ) -> Array: ...

    @staticmethod
    def matrix_transpose(x: Array, /) -> Array: ...

    @staticmethod
    def outer(x1: Array, x2: Array, /) -> Array: ...

    @staticmethod
    def pinv(x: Array, /, *, rtol: float | Array | None = None) -> Array: ...

    @staticmethod
    def qr(
        x: Array, /, *, mode: Literal["reduced", "complete"] = "reduced"
    ) -> tuple[Array, Array]: ...

    @staticmethod
    def slogdet(x: Array, /) -> tuple[Array, Array]: ...

    @staticmethod
    def solve(x1: Array, x2: Array, /) -> Array: ...

    @staticmethod
    def svd(
        x: Array, /, *, full_matrices: bool = True
    ) -> Array | tuple[Array, ...]: ...

    @staticmethod
    def svdvals(x: Array, /) -> Array: ...

    @staticmethod
    def tensordot(
        x1: Array,
        x2: Array,
        /,
        *,
        axes: int | tuple[Sequence[int], Sequence[int]] = 2,
    ) -> Array: ...

    @staticmethod
    def trace(x: Array, /, *, offset: int = 0) -> Array: ...

    @staticmethod
    def vecdot(x1: Array, x2: Array, /, *, axis: int = -1) -> Array: ...

    @staticmethod
    def vector_norm(
        x: Array,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
        ord: float = 2,
    ) -> Array: ...

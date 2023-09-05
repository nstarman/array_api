from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Literal, Protocol

if TYPE_CHECKING:
    # STDLIB
    from collections.abc import Sequence

    # LOCAL
    from array_api.array import ArrayAPI

__all__: list[str] = []


class ArrayAPILinAlgNamespace(Protocol):
    """Runtime-checkable protocol for linear algebra namespace."""

    @staticmethod
    def cholesky(x: ArrayAPI, /, *, upper: bool = False) -> ArrayAPI:
        ...

    @staticmethod
    def cross(x1: ArrayAPI, x2: ArrayAPI, /, *, axis: int = -1) -> ArrayAPI:
        ...

    @staticmethod
    def det(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def diagonal(x: ArrayAPI, /, *, offset: int = 0) -> ArrayAPI:
        ...

    @staticmethod
    def eigh(x: ArrayAPI, /) -> tuple[ArrayAPI]:
        ...

    @staticmethod
    def eigvalsh(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def inv(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def matmul(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def matrix_norm(
        x: ArrayAPI,
        /,
        *,
        keepdims: bool = False,
        ord: float | Literal["fro", "nuc"] | None = "fro",
    ) -> ArrayAPI:
        ...

    @staticmethod
    def matrix_power(x: ArrayAPI, n: int, /) -> ArrayAPI:
        ...

    @staticmethod
    def matrix_rank(
        x: ArrayAPI,
        /,
        *,
        rtol: float | ArrayAPI | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def matrix_transpose(x: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def outer(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def pinv(
        x: ArrayAPI,
        /,
        *,
        rtol: float | ArrayAPI | None = None,
    ) -> ArrayAPI:
        ...

    @staticmethod
    def qr(
        x: ArrayAPI,
        /,
        *,
        mode: Literal["reduced", "complete"] = "reduced",
    ) -> tuple[ArrayAPI, ArrayAPI]:
        ...

    @staticmethod
    def slogdet(x: ArrayAPI, /) -> tuple[ArrayAPI, ArrayAPI]:
        ...

    @staticmethod
    def solve(x1: ArrayAPI, x2: ArrayAPI, /) -> ArrayAPI:
        ...

    @staticmethod
    def svd(
        x: ArrayAPI,
        /,
        *,
        full_matrices: bool = True,
    ) -> ArrayAPI | tuple[ArrayAPI, ...]:
        ...

    @staticmethod
    def svdvals(x: ArrayAPI, /) -> ArrayAPI:
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
    def trace(x: ArrayAPI, /, *, offset: int = 0) -> ArrayAPI:
        ...

    @staticmethod
    def vecdot(x1: ArrayAPI, x2: ArrayAPI, /, *, axis: int = -1) -> ArrayAPI:
        ...

    @staticmethod
    def vector_norm(
        x: ArrayAPI,
        /,
        *,
        axis: int | tuple[int, ...] | None = None,
        keepdims: bool = False,
        ord: float = 2,
    ) -> ArrayAPI:
        ...

from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING

# LOCAL
from array_api.namespace import get_namespace

if TYPE_CHECKING:
    # LOCAL
    from array_api.array import ArrayAPIConformant
    from array_api.device import DeviceConformant
    from array_api.dtype import DTypeConformant

__all__: list[str] = []


def empty_like(
    x: ArrayAPIConformant, /, *, dtype: DTypeConformant | None = None, device: DeviceConformant | None = None
) -> ArrayAPIConformant:
    """
    Returns an uninitialized array with the same ``shape`` as an input array
    ``x``.

    Parameters
    ----------
    x: array
        input array from which to derive the output array shape.
    dtype: dype or None
        output array data type. If ``dtype`` is ``None``, the output array data
        type must be inferred from ``x``. Default: ``None``.
    device: device or None
        device on which to place the created array. If ``device`` is ``None``,
        the output array device must be inferred from ``x``. Default: ``None``.

    Returns
    -------
    out: array
        an array having the same shape as ``x`` and containing uninitialized
        data.
    """
    return get_namespace(x).empty_like(x, dtype=dtype, device=device)


def full_like(
    x: ArrayAPIConformant,
    /,
    fill_value: int | float,
    *,
    dtype: DTypeConformant | None = None,
    device: DeviceConformant | None = None,
) -> ArrayAPIConformant:
    """
    Returns a new array filled with ``fill_value`` and having the same ``shape``
    as an input array ``x``.

    Parameters
    ----------
    x: array
        input array from which to derive the output array shape.
    fill_value: int or float
        fill value.
    dtype: dype or None
        output array data type. If ``dtype`` is ``None``, the output array data
        type must be inferred from ``x``. Default: ``None``.

        .. note::

            If the ``fill_value`` exceeds the precision of the resolved output
            array data type, behavior is unspecified and, thus,
            implementation-defined.

        .. note::

            If the ``fill_value`` has a data type (``int`` or ``float``) which
            is not of the same data type kind as the resolved output array data
            type (see :ref:`type-promotion`), behavior is unspecified and, thus,
            implementation-defined.

    device: device or None
        device on which to place the created array. If ``device`` is ``None``,
        the output array device must be inferred from ``x``. Default: ``None``.

    Returns
    -------
    out: array
        an array having the same shape as ``x`` and where every element is equal
        to ``fill_value``.
    """
    return get_namespace(x).full_like(x, fill_value=fill_value, dtype=dtype, device=device)


def meshgrid(*arrays: ArrayAPIConformant, indexing: str = "xy") -> list[ArrayAPIConformant]:
    """
    Returns coordinate matrices from coordinate vectors.

    Parameters
    ----------
    arrays: array
        an arbitrary number of one-dimensional arrays representing grid
        coordinates. Each array should have the same numeric data type.
    indexing: str
        Cartesian ``'xy'`` or matrix ``'ij'`` indexing of output. If provided
        zero or one one-dimensional vector(s) (i.e., the zero- and
        one-dimensional cases, respectively), the ``indexing`` keyword has no
        effect and should be ignored. Default: ``'xy'``.

    Returns
    -------
    out: List[array]
        list of N arrays, where ``N`` is the number of provided one-dimensional
        input arrays. Each returned array must have rank ``N``. For ``N``
        one-dimensional arrays having lengths ``Ni = len(xi)``,

        - if matrix indexing ``ij``, then each returned array must have the
        shape ``(N1, N2, N3, ..., Nn)``. - if Cartesian indexing ``xy``, then
        each returned array must have shape ``(N2, N1, N3, ..., Nn)``.

        Accordingly, for the two-dimensional case with input one-dimensional
        arrays of length ``M`` and ``N``, if matrix indexing ``ij``, then each
        returned array must have shape ``(M, N)``, and, if Cartesian indexing
        ``xy``, then each returned array must have shape ``(N, M)``.

        Similarly, for the three-dimensional case with input one-dimensional
        arrays of length ``M``, ``N``, and ``P``, if matrix indexing ``ij``,
        then each returned array must have shape ``(M, N, P)``, and, if
        Cartesian indexing ``xy``, then each returned array must have shape
        ``(N, M, P)``.

        Each returned array should have the same data type as the input arrays.
    """
    return get_namespace(*arrays).meshgrid(*arrays, indexing=indexing)


def ones_like(
    x: ArrayAPIConformant, /, *, dtype: DTypeConformant | None = None, device: DeviceConformant | None = None
) -> ArrayAPIConformant:
    """
    Returns a new array filled with ones and having the same ``shape`` as an
    input array ``x``.

    Parameters
    ----------
    x: array
        input array from which to derive the output array shape.
    dtype: dype or None
        output array data type. If ``dtype`` is ``None``, the output array data
        type must be inferred from ``x``. Default: ``None``.
    device: device or None
        device on which to place the created array. If ``device`` is ``None``,
        the output array device must be inferred from ``x``. Default: ``None``.

    Returns
    -------
    out: array
        an array having the same shape as ``x`` and filled with ones.
    """
    return get_namespace(x).ones_like(x, dtype=dtype, device=device)


def tril(x: ArrayAPIConformant, /, *, k: int = 0) -> ArrayAPIConformant:
    """
    Returns the lower triangular part of a matrix (or a stack of matrices)
    ``x``.

    .. note::

        The lower triangular part of the matrix is defined as the elements on
        and below the specified diagonal ``k``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two
        dimensions form ``MxN`` matrices.
    k: int
        diagonal above which to zero elements. If ``k = 0``, the diagonal is the
        main diagonal. If ``k < 0``, the diagonal is below the main diagonal. If
        ``k > 0``, the diagonal is above the main diagonal. Default: ``0``.

        .. note::

            The main diagonal is defined as the set of indices ``{(i, i)}`` for
            ``i`` on the interval ``[0, min(M, N) - 1]``.

    Returns
    -------
    out: array
        an array containing the lower triangular part(s). The returned array
        must have the same shape and data type as ``x``. All elements above the
        specified diagonal ``k`` must be zeroed. The returned array should be
        allocated on the same device as ``x``.
    """
    return get_namespace(x).tril(x, k=k)


def triu(x: ArrayAPIConformant, /, *, k: int = 0) -> ArrayAPIConformant:
    """
    Returns the upper triangular part of a matrix (or a stack of matrices)
    ``x``.

    .. note::

        The upper triangular part of the matrix is defined as the elements on
        and above the specified diagonal ``k``.

    Parameters
    ----------
    x: array
        input array having shape ``(..., M, N)`` and whose innermost two
        dimensions form ``MxN`` matrices.
    k: int
        diagonal below which to zero elements. If ``k = 0``, the diagonal is the
        main diagonal. If ``k < 0``, the diagonal is below the main diagonal. If
        ``k > 0``, the diagonal is above the main diagonal. Default: ``0``.

        .. note::

            The main diagonal is defined as the set of indices ``{(i, i)}`` for
            ``i`` on the interval ``[0, min(M, N) - 1]``.

    Returns
    -------
    out: array
        an array containing the upper triangular part(s). The returned array
        must have the same shape and data type as ``x``. All elements below the
        specified diagonal ``k`` must be zeroed. The returned array should be
        allocated on the same device as ``x``.
    """
    return get_namespace(x).triu(x, k=k)


def zeros_like(
    x: ArrayAPIConformant, /, *, dtype: DTypeConformant | None = None, device: DeviceConformant | None = None
) -> ArrayAPIConformant:
    """
    Returns a new array filled with zeros and having the same ``shape`` as an
    input array ``x``.

    Parameters
    ----------
    x: array
        input array from which to derive the output array shape.
    dtype: dype or None
        output array data type. If ``dtype`` is ``None``, the output array data
        type must be inferred from ``x``. Default: ``None``.
    device: device or None
        device on which to place the created array. If ``device`` is ``None``,
        the output array device must be inferred from ``x``. Default: ``None``.

    Returns
    -------
    out: array
        an array having the same shape as ``x`` and filled with zeros.
    """
    return get_namespace(x).zeros_like(x, dtype=dtype, device=device)

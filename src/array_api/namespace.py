from __future__ import annotations

# STDLIB
from typing import TYPE_CHECKING, Any

# LOCAL
from array_api.array import ArrayAPIConformant

if TYPE_CHECKING:
    # LOCAL
    from array_api._types import ArrayAPINamespace

__all__: list[str] = []


def get_namespace(*xs: Any, api_version: str | None = None) -> ArrayAPINamespace:
    """Get the array API namespace for the given array inputs.

    Parameters
    ----------
    *xs : Any
        Input arrays for which to get the array API namespace.
    api_version : str | None, optional
        The array API version, by default `None`.

    Returns
    -------
    `~array_api._types.ArrayAPINamespace`
        The array API namespace for the given array inputs.

    Raises
    ------
    ValueError
        If none of the inputs are array API conformant.
        If the inputs are from multiple array API namespaces.
    """
    # `xs` contains one or more arrays.
    namespaces = {x.__array_namespace__(api_version=api_version) for x in xs if isinstance(x, ArrayAPIConformant)}

    if not namespaces:
        raise ValueError("Unrecognized array input")
    elif len(namespaces) != 1:
        raise ValueError(f"Multiple namespaces for array inputs: {namespaces}")

    return namespaces.pop()

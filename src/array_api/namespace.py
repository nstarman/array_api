"""Namespace utilities for array APIs."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from array_api.array import ArrayAPI

if TYPE_CHECKING:
    from array_api._types import ArrayAPINamespace

__all__: list[str] = []


def get_namespace(
    *xs: Any,  # noqa: ANN401
    api_version: str | None = None,
) -> ArrayAPINamespace:
    """
    Get the array API namespace for the given array inputs.

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
    namespaces: set[ArrayAPINamespace] = {
        x.__array_namespace__(api_version=api_version)
        for x in xs
        if isinstance(x, ArrayAPI)
    }

    if not namespaces:
        msg = "Unrecognized array input"
        raise ValueError(msg)
    if len(namespaces) != 1:
        msg = f"Multiple namespaces for array inputs: {namespaces}"
        raise ValueError(msg)

    return namespaces.pop()

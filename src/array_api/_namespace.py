"""Namespace utilities for array APIs."""

from __future__ import annotations

__all__ = ["get_namespace"]

from typing import TYPE_CHECKING, Any, Protocol, runtime_checkable

if TYPE_CHECKING:
    from array_api._namespace_api import ArrayAPINamespace


@runtime_checkable
class BaseTrait(Protocol):
    def __array_namespace__(
        self, *, api_version: str | None = ...
    ) -> ArrayAPINamespace: ...


def get_namespace(
    *xs: Any,  # noqa: ANN401
    array_traits: type | tuple[type, ...] = BaseTrait,
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

"""Constants."""

__all__ = ["e", "inf", "nan", "newaxis", "pi"]

from typing import Protocol

e: float = 2.71828182845904523536028747135266249775724709369995
# IEEE 754 floating-point representation of Euler's constant.
# ``e = 2.71828182845904523536028747135266249775724709369995...``


inf: float = float("inf")
# IEEE 754 floating-point representation of (positive) infinity.


nan: float = float("nan")
# IEEE 754 floating-point representation of Not a Number (``NaN``).


newaxis: None = None
# An alias for ``None`` which is useful for indexing arrays.


pi: float = 3.1415926535897932384626433832795028841971693993751
# IEEE 754 floating-point representation of the mathematical constant ``π``.
# ``pi = 3.1415926535897932384626433...``


###############################################################################


class HasConstants(Protocol):
    """Protocol for the constants in the Array API namespace."""

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

import math
from decimal import Decimal

a = math.sqrt(81)  # always returns a floating-point number (float)
print(a)  # 9.0

d = 0.1 + 0.2

# floating point rounding error: binary cannot represent some decimals exactly
# just like how base 10 cannot represent 1/3 = 0.333 exactly (infinite decimals -> rounding errors)
print(d)
print(d == 0.3)  # False!

# math gives you a function for comparing numbers in those cases
print(math.isclose(d, 0.1))  # returns True

"""
For critical workflows, use the Decimal class to overcome these limitations.
It uses extra software to simulate base 10 arithmetic.
Note that this is much slower than regular floating-point (FP) arithmetic.
"""

# the next line is a comment that tells PyCharm to ignore a warning. If you remove it, you'll see it.
# noinspection string-conversion-without-dunder-method
print(Decimal("0.1") + Decimal("0.2"))  # returns exactly Decimal('0.3')

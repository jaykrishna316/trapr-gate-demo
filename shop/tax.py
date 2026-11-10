# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Jayakrishna Ichapurapu
# ref: 67cd6530-515f4352
"""Sales tax."""


def with_tax(amount: float, rate: float = 0.0825) -> float:
    return round(amount * (1 + rate), 2)

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Jayakrishna Ichapurapu
# ref: 67cd6530-f7ee3388
"""Gift cards."""


def redeem(balance: float, amount: float) -> float:
    if amount > balance:
        raise ValueError("insufficient balance")
    return round(balance - amount, 2)

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Jayakrishna Ichapurapu
# ref: 67cd6530-2d0b2dc8
"""Discount rules applied at checkout."""


def percent_off(total: float, pct: float) -> float:
    if not 0 <= pct <= 100:
        raise ValueError("pct must be between 0 and 100")
    return round(total * (1 - pct / 100), 2)


def bulk_discount(qty: int, unit: float) -> float:
    tiers = [(100, 0.15), (50, 0.10), (10, 0.05)]
    for min_qty, rate in tiers:
        if qty >= min_qty:
            return round(qty * unit * (1 - rate), 2)
    return round(qty * unit, 2)

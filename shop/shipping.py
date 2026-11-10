"""Shipping cost by weight and zone."""

RATES = {"local": 4.0, "national": 7.5, "international": 19.0}


def shipping_cost(weight_kg: float, zone: str) -> float:
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    base = RATES[zone]
    extra = max(0.0, weight_kg - 1) * (base / 4)
    return round(base + extra, 2)

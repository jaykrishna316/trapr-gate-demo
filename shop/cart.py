"""A tiny shopping cart."""
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: dict = field(default_factory=dict)

    def add(self, sku: str, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("qty must be positive")
        self.items[sku] = self.items.get(sku, 0) + qty

    def remove(self, sku: str) -> None:
        self.items.pop(sku, None)

    def total(self, prices: dict) -> float:
        return round(sum(prices[s] * q for s, q in self.items.items()), 2)

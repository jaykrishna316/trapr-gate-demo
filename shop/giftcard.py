"""Gift cards."""


def redeem(balance: float, amount: float) -> float:
    if amount > balance:
        raise ValueError("insufficient balance")
    return round(balance - amount, 2)

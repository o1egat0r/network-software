# Машина состояний саги оформления профиля (profiles-s05).

from typing import Final

# Допустимые состояния: NEW, PAID, DONE, CANCELLED
_TRANSITIONS: Final[dict[tuple[str, str], str]] = {
    ("NEW", "PAY_OK"): "PAID",
    ("NEW", "PAY_FAIL"): "CANCELLED",
    ("PAID", "FULFILL_OK"): "DONE",
    ("PAID", "FULFILL_FAIL"): "CANCELLED",
    ("CANCELLED", "RELEASE_STOCK_RETRY_OK"): "CANCELLED",
}


def next_state(state: str, event: str) -> str:
    """Возвращает новое состояние; неизвестная пара (state, event) оставляет state без изменений."""
    return _TRANSITIONS.get((state, event), state)

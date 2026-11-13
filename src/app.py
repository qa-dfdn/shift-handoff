"""Shift handoff notes for Lumenfield Medical"""

class ShiftHandoff:
    """Internal service for shift-handoff."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(ShiftHandoff().status())

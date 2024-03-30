class Modifier:
    def __init__(self, text: str, value: float):
        self.text = text
        self.value = value

    def __str__(self) -> str:
        return f"<{self.text}|*{self.value}>"

    def is_modifier(self) -> bool:
        return True
    
class Base:
    def __init__(self, text: str, value: float):
        self.text = text
        self.base_value = value
        self._value = value
        self.modifiers = []

    def __str__(self) -> str:
        return f"<{self.text}|{'-' if self.base_value < 0 else '+'}{abs(self.base_value)}|{'-' if self._value < 0 else '+'}{abs(self._value)}>"

    def is_modifier(self) -> bool:
        return False
    
    def apply(self, modifier: Modifier, mask: float = 1):
        self.modifiers.append(modifier)
        self._value *= modifier.value * mask

    def value(self) -> float:
        return self._value

class Counter:
    """Клас цифрового лічильника з межами мінімуму та максимуму."""

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10):
        self.current: int = current
        self.min_value: int = min_value
        self.max_value: int = max_value

    def set_current(self, start: int) -> None:
        """Встановлює початкове значення лічильника."""
        self.current = start

    def set_max(self, max_max: int) -> None:
        """Встановлює максимальне значення лічильника."""
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """Встановлює мінімальне значення лічильника."""
        self.min_value = min_min

    def step_up(self) -> None:
        """Збільшує значення лічильника на 1."""
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self) -> None:
        """Зменшує значення лічильника на 1."""
        if self.current <= self.min_value:
            raise ValueError("Досягнутий мінімум")
        self.current -= 1

    def get_current(self) -> int:
        """Повертає поточне значення лічильника."""
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as e:
    print(e)

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)

assert counter.get_current() == 7, 'Test4'
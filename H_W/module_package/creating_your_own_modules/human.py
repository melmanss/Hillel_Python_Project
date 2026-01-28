class Human:
    """Клас, що описує людину."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender: str = gender
        self.age: int = age
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} років"
class AddParams:
    a: int
    b: int


def add(a: int, b: int) -> int:
    return a + b


result = add(5, 3)
print(f"Result: {result}")  # Output: Result: 8 (5 + 3 = 8, result)

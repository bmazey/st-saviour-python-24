def fibonacci_recursive(position: int) -> int:

    if position <= 1:
        return 1
    return fibonacci_recursive(position - 1) + fibonacci_recursive(position -2)
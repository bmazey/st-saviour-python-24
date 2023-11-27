def fibonacci(position: int) -> int:

    if position <= 1:
        return 1
    return fibonacci(position - 1) + fibonacci(position -2)
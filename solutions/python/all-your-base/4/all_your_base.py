def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:

    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if not all(0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    
    decimal = sum(d * input_base ** i for i, d in enumerate(reversed(digits))) # or enumerate(digits[::-1])

    new_digits = []
    while decimal > 0:
        new_digits.insert(0, decimal % output_base)
        decimal //= output_base

    return new_digits or [0]

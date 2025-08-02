def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:

    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if not all(0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    
    some_digits = sum(x * input_base ** i for i, x in zip(range(len(digits) -1, -1, -1), digits))
    new_digits = []
    while some_digits >= output_base:
        new_digits.append(some_digits % output_base)
        some_digits //= output_base
    new_digits.append(some_digits % output_base)
    new_digits = new_digits[::-1]

    return new_digits

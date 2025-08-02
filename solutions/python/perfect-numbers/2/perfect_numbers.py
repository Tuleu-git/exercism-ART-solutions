def classify(number: int) -> str:
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    num = sum([n for n in range(1, number) if number % n == 0])
    return 'perfect' if number == num else 'abundant' if number < num else 'deficient'
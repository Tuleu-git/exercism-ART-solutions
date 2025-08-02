def classify(number: int) -> str:
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    for i in range (1, number):
        if number % i == 0:
            sum += i
    return 'perfect' if number == sum else 'abundant' if number < sum else 'deficient'
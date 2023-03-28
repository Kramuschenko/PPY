def prime(*numbers):
    for number in numbers:
        if number < 2:
            print(f"{number} is not prime")
            continue
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is prime number")
        else:
            print(f"{number} is not prime")

prime(0, 1, 2, 3, 4, 5)
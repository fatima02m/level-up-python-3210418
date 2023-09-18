
# gets a list of prime factors
# strategy: divide number by 2, if no remainder then its a prime factor
# if yes remainder then, increment divisor by 1
#

def get_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1

    return factors


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(25))

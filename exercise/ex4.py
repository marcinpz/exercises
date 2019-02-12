import sys

USAGE = """
Program finds prime numbers with Eratostene sieve method.

Usage:
    {program} <max>  # finds prime numbers in range(2, max). max must be larger than 2
"""


def usage():
    usage_txt = USAGE.format(program=sys.argv[0])
    print(usage_txt)


def eratostene_sieve(max_number):
    assert max_number >= 2
    primes = list(range(2, max_number + 1))
    index = 0
    while True:
        if index >= len(primes):
            break
        x = primes[index]
        multiplications = list(range(x * 2, max_number + 1, x))
        primes = [i for i in primes if i not in multiplications]
        index += 1

    return primes


if __name__ == '__main__':
    if len(sys.argv) == 2:
        _max_number = int(sys.argv[1])
        print(eratostene_sieve(_max_number))
    else:
        usage()

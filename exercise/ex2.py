import sys


USAGE = """
Program finds Amstrong numbers in given range.

N digit Amstrong number is the number equal sum of N-th power of its digits.

Example:
    153 = 1^3 + 5^3 + 3^3  

Usage:
    {program} [[start] stop]
"""


def is_amstrong_number(x: int):
    digits = list(map(int, str(x)))
    return sum(map(lambda n: pow(n, len(digits)), digits)) == x


def usage():
    usage_txt = USAGE.format(program=sys.argv[0])
    print(usage_txt)


def exercise(_range):
    for number in _range:
        if is_amstrong_number(number):
            print(number)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        stop = int(sys.argv[1])
        _range = range(stop)
        exercise(_range)
    elif len(sys.argv) == 3:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
        _range = range(start, stop)
        exercise(_range)
    else:
        usage()

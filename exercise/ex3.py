import sys

USAGE = """
Program checks hyphotesis that for each natural number:
    - it is palindrom
    - or x += reversed(x) is palindrom (after some recursion)

Example:
    121 is palindrom because reversed is the same number
    78 because 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884 - is palindrom

Usage:
    {program} <MAX_RECURSIONS> [stop (200 by default)]
    
Test:
    {program} 1000  # test if hyphotesis is true for numbers in range(0, 200) - with max 1000 recursions 
"""


def is_palindrom(number):
    _str = str(number)
    return _str == _str[::-1]


def check_hyphotesis_is_true(number, max_recursions):
    x = number
    for i in range(max_recursions):
        if is_palindrom(x):
            return True
        else:
            reversed_x = int(str(x)[::-1])
            x += reversed_x
    return False


def usage():
    usage_txt = USAGE.format(program=sys.argv[0])
    print(usage_txt)


def exercise(max_recursions, max_value=200):
    for i in range(max_value):
        if check_hyphotesis_is_true(i, max_recursions):
            print(f"{i} - OK")
        else:
            print(f"{i} - FALSE!!!")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        _max_recursions = int(sys.argv[1])
        exercise(_max_recursions)
    elif len(sys.argv) == 3:
        _max_recursions = int(sys.argv[1])
        _stop = int(sys.argv[2])
        exercise(_max_recursions, _stop)
    else:
        usage()

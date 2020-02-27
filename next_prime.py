#!/usr/bin/env python
"""next_prime.py

Find the next prime number that comes after the user submitted
n, up to 1998, whose next prime is 1999."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys
import math

# hard limit on range
max_n = 1998

def isPrime(number):
    if number < 2:
        print("Error in isPrime: argument must be > 1")
        raise ValueError

    if number == 2:
        return True
    else:
        max_range = math.ceil(math.sqrt(number))
        isPrime = True
        i = 2
        while(isPrime):
            if number % i == 0:
                isPrime = False
            elif i > max_range:
                break
            else:
                i += 1

        return isPrime

def main():
    try:
        n = (int)(sys.argv[1])
        if n < 2:
            raise ValueError
        elif n >= 1999:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: next_prime.py [n]")
        print("[n] = an integer that is 2 or greater, up to 1998")
        sys.exit(1)

    # just answer if input is 2
    if n == 2:
        print(3)
        sys.exit(0)

    # iteration flag
    prime_found = False
    test_max = (n * 2)

    i = n + 1
    while(prime_found == False):
        if i == test_max:
            print("There has been a fatal programming error.")
            print("A prime should have been found but was not.")
            exit(1)
        prime_found = isPrime(i)
        if(prime_found):
            break
        elif i % 2 == 0:
            i += 1      # i is even, go to next odd
        else:
            i += 2      # i is odd, go to next odd
    
    print(i)

if __name__ == "__main__":
    main()

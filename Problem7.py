# Problem7.py
# Project Euler Problem 7 - Find the 10,001st prime

from NumberTests import getNthPrime

def main():
    prime = getNthPrime(10001)
    print(prime)  
if __name__ == '__main__':
    main()

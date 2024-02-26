"""
 * - Crea una función recursiva que imprima números del 100 al 0.
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def print_reverse_nums(n: int):
    if n == 0:
        print(0)
    else:
        print(n)
        print_reverse_nums(n - 1)


def calculate_factorial(n: int):
    if n == 1:
        return 1
    
    return n * calculate_factorial(n - 1)


def get_fibonacci_number(pos: int):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    
    return get_fibonacci_number(pos - 1) + get_fibonacci_number(pos - 2)


def main():
    print_reverse_nums(100)
    print(calculate_factorial(5))
    print(get_fibonacci_number(10))


if __name__ == "__main__":
    main()
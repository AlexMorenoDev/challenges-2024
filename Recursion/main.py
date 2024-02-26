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


def get_fibonacci_number_1(pos: int):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    
    return get_fibonacci_number_1(pos - 1) + get_fibonacci_number_1(pos - 2)


# Alternative function using a dictionary to avoid calculating numbers that has been already calculated
# With high numbers it is very efficient
def get_fibonacci_number_2(pos: int, calculated_nums: dict):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    
    if pos in calculated_nums:
        return calculated_nums[pos]
    else:
        current_pos_num = get_fibonacci_number_2(pos - 1, calculated_nums) + get_fibonacci_number_2(pos - 2, calculated_nums)
        calculated_nums[pos] = current_pos_num
        return current_pos_num


def main():
    print_reverse_nums(100)
    print(calculate_factorial(5))
    print(get_fibonacci_number_1(40)) # Execution time: 18-19 seconds
    print(get_fibonacci_number_2(40, {})) # Execution time: Instantly


if __name__ == "__main__":
    main()
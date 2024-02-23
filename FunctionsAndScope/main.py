"""
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def print_numbers(str1: str, str2: str):

    def is_multiple(num: int, mult: int):
        return num % mult == 0
    
    count = 0
    for i in range(1, 101):
        if is_multiple(i, 3) and is_multiple(i, 5):
            print(str1 + str2)
        elif is_multiple(i, 3):
            print(str1)
        elif is_multiple(i, 5):
            print(str2)
        else:
            print(i)
            count += 1

    return count
        

def main():
    print(print_numbers("Three", "Five"))


if __name__ == "__main__":
    main()
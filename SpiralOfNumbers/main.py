"""
* Imprime los números de 1 a N en formato espiral comenzando desde el centro
* y en sentido horario.
* La función que realice esta tarea tendrá como parámetro el tamaño del lado (s_length).
* N se podrá calcular de la siguiente manera: N = s_length^2
* 
* Ejemplo de salida para lado 5:
*   21 22 23 24 25
*   20 7  8  9  10
*   19 6  1  2  11
*   18 5  4  3  12
*   17 16 15 14 13
"""

def init_empty_matrix(s_length: int):
    matrix = []

    for _ in range(s_length):
        matrix.append([0] * s_length)

    return matrix


def get_mid_point(s_length: int):
    mid_point = int(s_length / 2)
    if s_length % 2 == 0:
        return mid_point - 1
    return mid_point


def get_next_direction(directions: list, directions_length: int, current_dir: str):
    dir_pos = directions.index(current_dir)
    if dir_pos == (directions_length - 1):
        return directions[0]
    return directions[dir_pos + 1]


def print_matrix(matrix: list, s_length: int):
    if s_length % 2 == 0:
        max_digits = len(matrix[-1][0])
    else:
        max_digits = len(matrix[0][-1])

    with open(f"results/result_{s_length}.txt", 'w') as textfile:
        for row in matrix:
            row_str = ""
            for i, num in enumerate(row):
                if i < (s_length-1):
                    # +1 is neccesary to add the space between numbers
                    row_str += (num + ' '*((max_digits-len(num))+1))
                else:
                    row_str += num
            print(row_str)
            textfile.write(row_str + '\n')


def draw_spiral(s_length: int):
    if s_length > 0:
        matrix = init_empty_matrix(s_length)
        mid_point = get_mid_point(s_length)
        directions = ['right', 'down', 'left', 'up']
        directions_length = len(directions)

        x, y = mid_point, mid_point
        matrix[y][x] = '1'
        current_dir = 'right'
        
        i = 2
        step = 1 
        count = 0
        while i <= (s_length**2):
            match current_dir:
                case 'right':
                    x += 1
                case 'down':
                    y += 1
                case 'left':
                    x -= 1
                case 'up':
                    y -= 1
            
            matrix[y][x] = str(i)
            i += 1
            count += 1
            
            if count == step:
                current_dir = get_next_direction(directions, directions_length, current_dir)
                if current_dir == 'right' or current_dir == 'left':
                    step += 1
                count = 0
                
        print_matrix(matrix, s_length)
    else:
        print("")


def main():
    draw_spiral(3)
    print("--------------------")
    draw_spiral(5)
    print("--------------------")
    draw_spiral(10)


if __name__ == "__main__":
    main()
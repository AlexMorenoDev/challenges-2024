"""
 * Implementa dos clases que representen las estructuras de Pila y Cola.
 * - Deben poder inicializarse y disponer de operaciones para añadir, 
 *   eliminar (retornar el elemento eliminado), retornar el número total 
 *   de elementos e imprimir todo su contenido.
"""

class Stack:
    def __init__(self, elements: list=[]):
        self.elements = elements
        self.length = len(elements)

    def add(self, val: int):
        self.elements.append(val)
        self.length += 1

    def get(self):
        if self.length > 0:
            self.length -= 1
            return self.elements.pop(-1)
        return None

    def length(self):
        return self.length

    def print_content(self):
        print("Stack content:")
        for el in reversed(self.elements):
            print("\t" + str(el))


class Queue:
    def __init__(self, elements: list=[]):
        self.elements = elements
        self.length = len(elements)

    def add(self, val: int):
        self.elements.append(val)
        self.length += 1

    def get(self):
        if self.length > 0:
            self.length -= 1
            return self.elements.pop(0)
        return None

    def length(self):
        return self.length

    def print_content(self):
        print("Queue content:")
        formatted_str = ""
        for i, el in enumerate(self.elements):
            formatted_str += str(el)
            if i < (self.length-1):
                formatted_str += " | "
        print(formatted_str)


def main():
    stack = Stack()
    queue = Queue()
    for i in range(1, 7):
        stack.add(i)
        queue.add(i)

    stack.print_content()
    print(f"Stack length: {stack.length}\n")
    queue.print_content()
    print(f"Queue length: {queue.length}")

    print("----------------")
    print(f"Element got from stack: {stack.get()}")
    print(f"Element got from queue: {queue.get()}")
    print("----------------")

    stack.print_content()
    print(f"Stack length: {stack.length}\n")
    queue.print_content()
    print(f"Queue length: {queue.length}")
        

if __name__ == "__main__":
    main()
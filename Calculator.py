from Operations.Add import *
from Operations.Subtract import *
from Operations.Multiply import *
from Operations.Divide import *

# Import additional operation imports above


# In python, functions are considered objects. This means you
# can store them like variables using just their name and call
# them later by adding a () at the end.

# This list stores function names
operations = [add,
              subtract,
              multiply,
              divide]

# TODO: Implement operations in their own filed. Make each function return their resulting values.

def run():
    # each operation takes 2 numbers and will do what it wants with it
    while (line := input("Enter an Operation: ")).lower() != "quit":
        operation_found = False

        for operation in operations:

            if operation.__name__.lower() == line.lower():
                operand_1 = input("Enter the first value: ")
                operand_2 = input("Enter the second value: ")
                print(operation(float(operand_1), float(operand_2)))
                operation_found = True

        if not operation_found:
            print('\033[93m' + "Invalid Operation" + '\033[0m')

        print('\n')

    print("Calculator Exited")


if __name__ == '__main__':
    run()
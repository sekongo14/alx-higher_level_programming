#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    L = len(sys.argv)
    from calculator_1 import add, mul, div, sub
    if L != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operateur == '*':
            result = mul(a, b)
        elif operateur == '/':
            result = div(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))

import sys
import math

def main(b_sqared=None):
    command = sys.argv[1]

    if command == "add":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x + y)

    if command == "sub":
        x = int(sys.argv[2])
        y = int(sys.argv[3])

        print(x - y)

    if command == 'countto':
        x = int(sys.argv[2])
        for i in range(x):
            print(i)

    if 'hypot' == command:
        a = int(sys.argv[2])
        b = int(sys.argv[3])

        print (pyth(a,b))


def pyth(a, b):
        a_sqared = math.pow(a, 2)
        b_sqared = math.pow(b, 2)
        return math.sqrt(a_sqared + b_sqared)
main()

import turtle


def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)


def make_square(dave):
    lenght = int(input('tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, 100)


def make_line_and_turn(dave, length):
    dave.forward(len)
    dave.left(90)


# if __name__ == '__main__'
main()

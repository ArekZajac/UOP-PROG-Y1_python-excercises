# Exercises week 01


def say_name():
    print("Arek")


def say_hello_2():
    print("Hello")
    print("World")


def euros_2_pounds():
    euros = float(input("Euros: "))
    print("Pounds: ", 1.13 * euros)


def add_up():
    print("Total: ", (float(input("Number 1: "))) + (float(input("Number 2: "))))


def change_counter():
    coin1 = float(input("1p coins: "))
    coin2 = float(input("2p coins: "))
    coin5 = float(input("5p coins: "))
    print("Total: ", coin1 + (coin2 * 2) + (coin5 * 5))


def ten_hellos():
    for i in range(10):
        print("Hello")


def count_2():
    for y in range(10):
        print(y + 1)


def weights_table():
    print("kg       lb")
    for u in range(10):
        print((u + 1) * 10, "     ", ((u + 1) * 10) * 2.2)


def future_value():
    init_val = float(input("Initial Value: "))
    years = int(input("Years: "))
    for k in range(years):
        init_val = init_val * 1.055
    print(init_val)

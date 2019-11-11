# exercises week 05

import graphics as g
import matplotlib.pyplot as plt


def personal_greeting():
    print("Hello", input("Enter your name:"), "nice to see you!")


def formal_name():
    first = input("First Name:")
    last = input("Last Name:")
    print(first[:1] + "." + last)


def kilos_2_pounds():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print(round(kilos, 2), "kilos is equal to", round(pounds, 2), "pounds")


def email():
    first = input("First Name:")
    last = input("Last Name:")
    year = input("Year")
    print(last[:3] + "." + first[:1] + "." + year[2:] + "@myport.ac.uk")


def grade_test():
    grade = int(input("Enter grade:"))
    print('FFFFCCBBAAA'[grade])


def graphic_letters():
    word = input("Enter a word:")
    win = g.GraphWin("graphic_letters", 1000, 700)
    while 1:
        for i in word:
            m = win.getMouse()
            letter = g.Text(g.Point(m.getX(), m.getY()), i)
            letter.setSize(30)
            letter.draw(win)


def sing_a_song():
    word = input("Enter a word: ")
    length = int(input("Length: "))
    height = int(input("Height: "))
    for i in range(height):
        for j in range(length):
            print(word, end=" "),
        print()


def exchange_table():
    print("€         £")
    for i in range(20):
        i = float(i)
        pound = i * 1.13
        print("{0:0.2f}{1:10.2f}".format(i, pound))


def make_acronym():
    phrase = input("Enter phrase: ").split()
    for i in phrase:
        print(i[:1].upper(), end=" ")


def name_to_number():
    name = input("Enter a name: ")
    output = 0
    for i in name.lower():
        output = output + (ord(i) - 96)
    print(output)


def file_in_caps():
    f = open("dummy.txt", "r")
    print(f.read().upper())
    f.close()


def rainfall_chart():
    f = open("rainfall.txt", "r")
    for line in f:
        print(line.split(" ", 1)[0], end=" ")
        for i in range(20 - len(line.split(" ", 1)[0])):
            print(" ", end="")
        for j in range(int(line.split(" ", 1)[-1])):
            print("*", end="")
        print()
    f.close()


def rainfall_inches():
    f_a = open("rainfall.txt", "r")
    f_b = open("rainfall_inches.txt", "w")
    for line in f_a:
        f_b.write(str(line.split(" ", 1)[0]))
        f_b.write(" ")
        f_b.write(str(round(float(line.split(" ", 1)[-1]) / 25.4, 2)))
        f_b.write("\n")
    f_a.close()
    f_b.close()


def graphical_rainfall_chart():
    plt.figure(figsize=(15, 5))
    f = open("rainfall.txt", "r")
    places = []
    rain_amount = []
    positions = []
    count = 0
    for line in f:
        count += 1
        positions.append(count)
        places.append(line.split(" ", 1)[0])
        rain_amount.append(float(line.split(" ", 1)[-1]))
    plt.bar(positions, rain_amount)
    plt.xticks(positions, places)
    plt.show()
    f.close()


def wc():
    with open(input("File: ")) as file:
        lines = 0
        words = 0
        characters = 0
        for line in file:
            word_list = line.split()
            lines += 1
            words += len(word_list)
            characters += sum(len(word) for word in word_list)
    print(lines, "Lines")
    print(words, "Words")
    print(characters, "Characters")
    file.close()

"""

Exercise 1:

    - Objective: Create a class which represents people.
    - Requirements:
        1) The class attributes must be: name, age, height;
        2) The class must have public methods for sets and gets;
        3) The class must have a method for printing people's data.

    Reference: Course "Programação em Python do Básico ao Avançado" - Geek University, Udemy.

"""


class Person:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def person_information(self):
        print(
            f'Nome: {self.__name}\n'
            f'Idade: {self.__age} anos\n'
            f'Altura: {self.__height} cm'
        )


person1 = Person('Albert Einstein', '42', '175')

person1.person_information()

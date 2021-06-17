"""

Exercise 1:

    - Objective: Create a system which receives three integer values and print their sum.

    # Reference: Course "Programação em Python do Básico ao Avançado" - Geek University, Udemy. #

"""

print("Choisissez une option de langue, s'il vous plaît!\n"
      "Please, choose a language option!\n\n"
      "[1] - Français\n"
      "[2] - English\n")

try:

    option = int(input("Option: "))

    if option == 1:

        print("\nBienvenue! Saisissez trois valeurs ci-dessous pour voir leur somme.\n")
        first_value = int(input("Premier Valeur: "))
        second_value = int(input("Deuxième Valeur: "))
        third_value = int(input("Troisième Valeur: "))
        print(f"\nTotal = {first_value + second_value + third_value}")

    elif option == 2:

        print("\nWelcome! Please, enter three values below to see their sum.\n")
        first_value = int(input("First Value: "))
        second_value = int(input("Second Value: "))
        third_value = int(input("Third Value: "))
        print(f"\nTotal = {first_value, + second_value + third_value}")

    else:
        print("\nOption invalide! Redémarrez le système et choisissez une option valable, s'il vous plaît!"
              "\nInvalid option! Please, restart the system and choose a valid option!")

except ValueError:

    print("\nOption invalide! Redémarrez le système et choisissez une option valable, s'il vous plaît!"
          "\nInvalid option! Please, restart the system and choose a valid option!")

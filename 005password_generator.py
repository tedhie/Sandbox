from random import randint

version = 0.1
name = "P455w0Rd G3neRaT0r"

# Choices
letters = "abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
umlauts = "åäöÅÄÖ"
numbers = "1234567890"*5
symbols = "!@#%&=?"*7

# Welcome message
print(f"Welcome to the {name} version: {version}")

# Main loop
while True:
    # reset main string
    main_string = letters
    # Inputs
    if input("Do you want umlauts? (Y/N) ") in ["Y", "y"]:
        main_string = main_string + umlauts
    if input("Do you want numbers? (Y/N) ") in ["Y", "y"]:
        main_string = main_string + numbers
    if input("Do you want symbols? (Y/N) ") in ["Y", "y"]:
        main_string += symbols
    length = int(input("How long should the password be? "))

    # Generation
    while True:
        password = ""
        for i in range(0, length):
            password += main_string[randint(0, len(main_string)-1)]
        print(f"\nYour password is {password}")

        # Regeneration check
        if input(f"Regenerate? (Y/N) ") not in ["Y", "y"]:
            break

    # New parameters check
    if input(f"New parameters? (Y/N) ") not in ["Y", "y"]:
        break

print(f"Thanks for using {name}")

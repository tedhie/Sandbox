while True:
    user_input = input("")
    if "+" in user_input:
        split = user_input.split("+")
        calculated = int(split[0]) + int(split[1])
        print(calculated)
    elif "-" in user_input:
        split = user_input.split("-")
        calculated = int(split[0]) - int(split[1])
        print(calculated)
    elif "*" in user_input:
        split = user_input.split("*")
        calculated = int(split[0]) * int(split[1])
        print(calculated)
    elif "/" in user_input:
        split = user_input.split("/")
        calculated = int(split[0]) / int(split[1])
        print(calculated)

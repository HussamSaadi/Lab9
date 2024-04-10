


def encode(password):
    new_pass = []
    for item in password:
        item = int(item)
        item += 3
        new_pass.append(item)
    return new_pass
def decode(password):
    new_pass =[]
    password =""
    for item in password:
        item = int(item)
        item -= 3
        new_pass.append(item)
    return new_pass


def main():
    new_pass =[]
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        sel = int(input("Please enter an option: "))
        if sel == 1:
            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif sel ==2:
            new =""
            for item in new_pass:
                new = new + str(item)
            print(f"The encoded password is {new}, and the original password is {password}.")
        elif sel == 3:
            break

if __name__ == '__main__':
    main()
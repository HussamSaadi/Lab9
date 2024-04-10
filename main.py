


def encode(password):
    new_pass = []
    for item in password:
        item = int(item)
        item += 3
        if item >= 10:
            item = item -10
        new_pass.append(item)
    return new_pass
def decode(password):
    new_pass = []
    for item in password:
        item = int(item)
        item -= 3
        if item <= 0:
            item += 10
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
            new_str = ""
            orig_pass =""
            new = decode(new_pass)
            for item in new_pass:
                new_str += str(item)
            for item in new:
                orig_pass += str(item)


            print(f"The encoded password is {new_str}, and the original password is {orig_pass}.")
        elif sel == 3:
            break

if __name__ == '__main__':
    main()